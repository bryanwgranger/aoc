from collections import defaultdict
with open("dec7_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

def card_rank(c):
    strength = list("23456789TJQKA")
    return strength.index(c)

def card1_greater(card1, card2):
    for i in range(5):
        if card_rank(card1[i]) > card_rank(card2[i]):
            return True
        elif card_rank(card1[i]) < card_rank(card2[i]):
            return False

#hands
#five  6
#four 5
#full 4
#three 3
#twopair 2
#onepair 1
#highcard 0

def hand_type(hand):
    #card matches
    hand_dict = defaultdict(int)
    for c in hand:
        hand_dict[c] += 1
    vals = hand_dict.values()
    if 5 in vals:
        return 6
    elif 4 in vals:
        return 5
    elif 3 in vals:
        if 2 in vals:
            return 4
        else:
            return 3
    elif 2 in vals:
        if len(vals) == 3:
            return 2
        elif len(vals) == 4:
            return 1

    return 0

big_dict = defaultdict(list)
for l in lines:
    hand, bid = l.split()
    big_dict[hand_type(hand)].append((hand, bid))

for k,v in big_dict.items():
    for i in range(len(v)):
        sort = True
        for j in range(len(v)-i-1):
            if card1_greater(v[j][0], v[j+1][0]):
                v[j+1], v[j] = v[j], v[j+1]
                sort = False
        if sort:
            break

big_list = []
for i in range(7):
    big_list += big_dict[i]

total = 0
for r, hand in enumerate(big_list):
    total += (r + 1) * int(hand[1])
print("answer part one:", total)
###part two


def card_rank_pt2(c):
    strength = list("J23456789TQKA")
    return strength.index(c)

def card1_greater(card1, card2):
    for i in range(5):
        if card_rank_pt2(card1[i]) > card_rank_pt2(card2[i]):
            return True
        elif card_rank_pt2(card1[i]) < card_rank_pt2(card2[i]):
            return False

#hands
#five  6
#four 5
#full 4
#three 3
#twopair 2
#onepair 1
#highcard 0

def hand_type(hand):
    #card matches
    hand_dict = defaultdict(int)
    for c in hand:
        hand_dict[c] += 1
    vals = hand_dict.values()
    if 5 in vals:
        return 6
    elif 4 in vals:
        if "J" in hand:
            return 6
        return 5
    elif 3 in vals: #3,2 or #3,1,1
        if 2 in vals: #3,2
            if "J" in hand:
                return 6
            return 4
        else:
            if "J" in hand: #four of kind  - better than full house
                return 5
            return 3 #three of kind
    elif 2 in vals:
        if len(vals) == 3: #2,2,1
            if "J" in hand:
                if hand_dict["J"] > 1:
                    return 5 #four of kind
                return 4 #full house
            return 2
        elif len(vals) == 4: #2,1,1,1
            if "J" in hand:
                return 3
            return 1
    if "J" in hand:
        return 1
    return 0


big_dict = defaultdict(list)
for l in lines:
    hand, bid = l.split()
    big_dict[hand_type(hand)].append((hand, bid))

for k,v in big_dict.items():
    for i in range(len(v)):
        sort = True
        for j in range(len(v)-i-1):
            if card1_greater(v[j][0], v[j+1][0]):
                v[j+1], v[j] = v[j], v[j+1]
                sort = False
        if sort:
            break

big_list = []
for i in range(7):
    big_list += big_dict[i]

total = 0
for r, hand in enumerate(big_list):
    total += (r + 1) * int(hand[1])
print("answer part two:", total)
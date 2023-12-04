with open("dec4_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

part_one = 0
card_info_dict = {}

for i, line in enumerate(lines):
    card, numbers = line.split(":")
    card_idx = int(card.split()[-1])
    winning_numbers = [int(n) for n in numbers.split("|")[0].split()]
    card_numbers = [int(n) for n in numbers.split("|")[1].split()]

    card_score = 0
    count = 0
    for w in winning_numbers:
        if w in card_numbers:
            count += 1

    card_score = 2 ** (count-1) if count > 0 else 0
    part_one += card_score

    card_info_dict.update({card_idx: count})

print("answer part one:", part_one)

total_cards = {k:1 for k in card_info_dict.keys()}

for card in card_info_dict.keys():
    for j in range(total_cards[card]):
        for i in range(card_info_dict[card]):
            if card+i+1 in card_info_dict.keys():
                total_cards[card+i+1] += 1

print("answer part two:", sum(total_cards.values()))
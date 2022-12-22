with open('dec3.txt', 'r') as f:
    lines = [t.strip() for t in f.readlines()]

score_str = 'abcdefghijklmnopqrstuvwxyz'
answer_one = 0
answer_two = 0

for i, l in enumerate(lines):
    l_one, l_two = l[:int((len(l)/2))], l[int(len(l)/2):]
    common = [l for l in l_one if l in l_two][0]
    if common.islower():
        answer_one += score_str.find(common) + 1
    elif common.isupper():
        answer_one += (score_str.find(common.lower()) + 1) + 26

    if i + 1 < len(lines) and i % 3 == 0:
        set_one = l
        set_two = lines[i+1]
        set_three = lines[i+2]

        badge = [g for g in set_one if g in set_two and g in set_three][0]
        if badge.islower():
            answer_two += score_str.find(badge) + 1
        elif badge.isupper():
            answer_two += score_str.find(badge.lower()) + 1 + 26

print("answer 1:", answer_one)
print("answer 2:", answer_two)
with open("dec2_2024.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

safe = 0
safe_part_two = 0

def safe_check(seq):
    diffs = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    if abs(max(diffs)) > 3 or abs(min(diffs)) > 3:
        return 0
    if 0 in diffs:
        return 0
    signs = ["pos" if x > 0 else "neg" for x in diffs]
    if len(set(signs)) != 1:
        return 0
    return 1

for l in lines:
    seq = [int(s) for s in l.split()]
    result = safe_check(seq)
    safe += result
    if result == 0:
        safe_part_two_check = False
        for j in range(len(seq)):
            new_l = seq[:j] + seq[j + 1:]
            if safe_check(new_l) == 1:
                safe_part_two_check = True
                break
        if safe_part_two_check:
            safe_part_two += 1
print("part 1:", safe)
print("part 2:", safe_part_two + safe)

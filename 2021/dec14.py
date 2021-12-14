from collections import defaultdict

with open('dec14.txt') as f:
    lines = [t.strip() for t in f.readlines()]

compound = lines[0]
print(compound)

encode = {}

for line in lines[2:]:
    k = line.split('->')[0].strip()
    v = line.split('->')[1].strip()
    encode[k] = v

pair_counts = defaultdict(int)

for i in range(len(compound)-1):
    pair = compound[i:i+2]
    pair_counts[pair] += 1

compound_counts = defaultdict(int)

for j in range(40):
    temp = defaultdict(int)
    for i, item in enumerate(pair_counts.items()):
        pair = item[0]
        quantity = item[1]
        temp[pair[0] + encode[pair]] += quantity
        temp[encode[pair] + pair[1]] += quantity

    pair_counts = temp

    if j == 9:
        for pair, quantity in pair_counts.items():
            compound_counts[pair[0]] += quantity
        compound_counts[lines[0][-1]] += 1
        cc1 = sorted(compound_counts.items(), key=lambda x: x[1], reverse=True)
        print('part 1:')
        print(cc1[0][1] - cc1[-1][1])


compound_counts_pt2 = defaultdict(int)
for pair, quantity in pair_counts.items():
    compound_counts_pt2[pair[0]] += quantity
compound_counts_pt2[lines[0][-1]] += 1

cc2 = sorted(compound_counts_pt2.items(), key=lambda x: x[1], reverse=True)
print('part 2:')
print(cc2[0][1] - cc2[-1][1])

import re
with open("dec3_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

symbols = []
nums = []
num_dict = {}
num_values = {}

for i, l in enumerate(lines):
    for j, ch in enumerate(l):
        if not ch.isdigit() and ch != ".":
            symbols.append((i,j))
        elif ch.isdigit():
            nums.append((i,j))
            if j == 0 or not l[j-1].isdigit():
                num = re.match(r"\d{1,3}", l[j:]).group(0)
                num_values[(i,j)] = num
                num_dict[(i,j)] = []
                for q in range(len(str(num))):
                    num_dict[(i,j)].append((i,j+q))


gears = []
for i, l in enumerate(lines):
    for j, ch in enumerate(l):
        if ch == "*":
            gears.append((i,j))

matches = []
gear_dict ={}
for s in symbols:
    s_i, s_j = s
    if s in gears:
        gear_dict[s] = []
    for n in nums:
        if n[0] in [s_i-1,s_i,s_i+1] and n[1] in [s_j-1,s_j,s_j+1]:
            matches.append(n)
            if s in gear_dict.keys():
                gear_dict[s].append(n)

match_list = []
for k, v in num_dict.items():
    match = False
    for pt in v:
        if pt in matches:
            match = True
    if match:
        match_list.append(k)

part_one = 0
for k in match_list:
    part_one += int(num_values[k])
print("answer part one:",part_one)

double_gear_list = []
for g, vals in gear_dict.items():
    g_list = set()
    for n, pts in num_dict.items():
        for v in vals:
            if v in pts:
                g_list.add(n)
    if len(g_list) == 2:
        double_gear_list.append(g)

new_gear = {}
for g,v in gear_dict.items():
    if g in double_gear_list:
        new_gear[g] = []
        for n,pts in num_dict.items():
            for pt in v:
                if pt in pts:
                    if n not in new_gear[g]:
                        new_gear[g].append(n)

part_2 = 0
for g, v in new_gear.items():
    part_2 += int(num_values[v[0]]) * int(num_values[v[1]])
print("answer part two:", part_2)

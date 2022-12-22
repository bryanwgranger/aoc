from collections import defaultdict
with open('dec7.txt', 'r') as f:
    lines = [t.strip() for t in f.readlines()]

print(lines)
#
dir = defaultdict(int)
subs = defaultdict(list)
all_dirs = []

#dir = {}
current_line = 0
current_dir = "/"

parents = []
while (current_line < len(lines)):
    line = lines[current_line]

    if line.startswith("$ cd"):
        c = line.split(" ")[-1]
        if c != "..":
            current_dir = c
        print(current_dir)
        # if current_dir not in dir.keys():
        #     dir[current_dir]

    if line.startswith("dir"):
        new_dir = line.split(" ")[-1]
        print("new dir:", new_dir)
        subs[current_dir].append(new_dir)
        parents.append((current_dir, new_dir))

    if line[0].isdigit():
        value = int(line.split(" ")[0])
        dir[current_dir] += value




    current_line += 1

print(subs)
print(dir.keys())
print(parents)
print(len(parents))

for pair in parents:
    if pair[0] == 'wtvfgcrq':
        print(pair)
# new_dict = defaultdict(int)
# while parents:
#     pair = parents.pop(-1)
#     new_dict[pair[0]] += dir[pair[1]]


#add up all folders that have no subfolders and under 100k
first_total = 0

for d in list(dir.keys()):
    if d not in subs.keys():
        if dir[d] <= 100000:
            first_total += dir[d]

print(first_total)
    # else:
    #     folder_val = dir[d]
    #     for subfolder in subs[d]:
    #         folder_val += dir[subfolder]
    #     if folder_val <= 100000:
    #         total += folder_val

second_total = 0
second_dict = defaultdict(int)
while parents:
    pair = parents.pop(-1)
    second_dict[pair[0]] += dir[pair[1]]

for s in second_dict.keys():
    second_dict[s] += dir[s]
    if second_dict[s] <= 100000:
        second_total += second_dict[s]

print(second_total)

print(first_total + second_total)
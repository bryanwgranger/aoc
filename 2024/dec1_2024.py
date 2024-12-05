with open("dec1_2024.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

first_list = []
second_list = []
for l in lines:
    first, second = l.split()
    first_list.append(int(first))
    second_list.append(int(second))

first_sort = sorted(first_list)
second_sort = sorted(second_list)

sum = 0
for f, s in zip(first_sort, second_sort):
    sum += abs(f-s)
print("part one:", sum)

#part two
from collections import Counter
c1 = Counter(first_list)
c2 = Counter(second_list)

sim_score = 0
for f in first_list:
    sim_score += f * c2[f]
print("part two:", sim_score)
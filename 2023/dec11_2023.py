with open("dec11_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

gal_rows = []
gal_cols = []
galaxies = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "#":
            gal_cols.append(x)
            gal_rows.append(y)
            galaxies.append((x,y))

blank_cols = [j for j in range(len(lines[0])) if j not in set(gal_cols)]
blank_rows = [i for i in range(len(lines)) if i not in set(gal_rows)]

def galaxy_distance(gal1, gal2, part2):
    gal_x_diff = abs(gal2[0]-gal1[0])
    gal_y_diff = abs(gal2[1]-gal1[1])
    for x in blank_cols:
        if x < max(gal1[0], gal2[0]) and x > min(gal1[0], gal2[0]):
            if part2:
                gal_x_diff += 999999
            else:
                gal_x_diff += 1
    for y in blank_rows:
        if y < max(gal1[1], gal2[1]) and y > min(gal1[1], gal2[1]):
            if part2:
                gal_y_diff += 999999
            else:
                gal_y_diff += 1
    return gal_x_diff + gal_y_diff

from itertools import combinations
comb = [p for p in combinations(galaxies, r=2)]

part_one = 0
part_two = 0
for g, other_g in comb:
        part_one += galaxy_distance(g, other_g, part2=False)
        part_two += galaxy_distance(g, other_g, part2=True)
print("answer part one:", part_one)
print("answer part two:", part_two)
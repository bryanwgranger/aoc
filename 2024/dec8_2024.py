from collections import defaultdict
import numpy as np
with open("dec8_2024.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

grid = [list(l) for l in lines]

antennas = defaultdict(list)
antinodes = set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] != ".":
            antennas[grid[r][c]].append((r,c))

part1_antinodes = set()
antinodes = set()
for symbol in antennas.keys():
    for i, point1 in enumerate(antennas[symbol]):
        antinodes.add(point1)
        for j, point2 in enumerate(antennas[symbol]):
            antinodes.add(point2)
            if i != j:
                #print(point2, point1)
                slope = (point2[0]-point1[0])/(point2[1]-point1[1])
                dc = abs(point2[1]-point1[1])
                dr = abs(point2[0]-point1[0])
                #negative slope here is positive in real life
                pts = [point1, point2]
                #print(pts)
                if slope < 0:
                    top_index = np.argmax([p[1] for p in pts])
                    top_point = pts[top_index]
                    bottom_index = 1 if top_index == 0 else 0
                    bottom_point = pts[bottom_index]
                    antinode_top = (top_point[0] - dr, top_point[1] + dc)
                    antinode_bottom = (bottom_point[0] + dr, bottom_point[1] - dc)
                    for antinode in [antinode_top, antinode_bottom]:
                        if 0 <= antinode[1] < len(grid[0]) and 0 <= antinode[0] < len(grid):
                            part1_antinodes.add(antinode)
                            antinodes.add(antinode)
                    while (antinode_top[0] - dr >= 0 and antinode_top[1] + dc < len(grid[0])):
                        antinode_top = (antinode_top[0] - dr, antinode_top[1] + dc)
                        antinodes.add(antinode_top)
                    while (antinode_bottom[0] + dr < len(grid) and antinode_bottom[1] - dc >= 0):
                        antinode_bottom = (antinode_bottom[0] + dr, antinode_bottom[1] - dc)
                        antinodes.add(antinode_bottom)
                elif slope > 0:
                    bottom_index = np.argmax([p[1] for p in pts])
                    bottom_point = pts[bottom_index]
                    top_index = 1 if bottom_index == 0 else 0
                    top_point = pts[top_index]
                    antinode_top = (top_point[0] - dr, top_point[1] - dc)
                    antinode_bottom = (bottom_point[0] + dr, bottom_point[1] + dc)
                    # print(symbol, slope, top_point, (dr, dc), antinode_top)
                    # print(symbol, slope, bottom_point, (dr, dc), antinode_bottom)
                    for antinode in [antinode_top, antinode_bottom]:
                        if 0 <= antinode[1] < len(grid[0]) and 0 <= antinode[0] < len(grid):
                            part1_antinodes.add(antinode)
                            antinodes.add(antinode)
                    while antinode_top[0] - dr >= 0 and antinode_top[1] - dc >= 0:
                        antinode_top = (antinode_top[0] - dr, antinode_top[1] - dc)
                        antinodes.add(antinode_top)
                    while antinode_bottom[0] + dr < len(grid) and antinode_bottom[1] + dc < len(grid[0]):
                        antinode_bottom = (antinode_bottom[0] + dr, antinode_bottom[1] + dc)
                        antinodes.add(antinode_bottom)
                else:
                    print("slope = 0")

print("part1:", len(part1_antinodes))
print("part2:", len(antinodes))
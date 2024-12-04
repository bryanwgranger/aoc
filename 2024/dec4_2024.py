with open("dec4_2024.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)

grid = []
for l in lines:
    grid_row = []
    for ch in l:
        grid_row.append(ch)
    grid.append(grid_row)

count = 0
count_part_two = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        #1 horizontal
        if j <= len(row)-4 and "".join(row[j:j+4]) in ["XMAS", "SAMX"]:
            count += 1
        #2 vertical
        if i <= len(grid)-4 and "".join([grid[i+x][j] for x in range(4)]) in ["XMAS", "SAMX"]:
            count += 1
        #3 diagonal 1 (neg slope)
        if i <= len(grid)-4 and j <= len(row)-4 and "".join([grid[i+x][j+x] for x in range(4)]) in ["XMAS", "SAMX"]:
            count += 1
            # 3 diagonal 1 (neg slope)
        if i <= len(grid)-4 and j >= 3 and "".join([grid[i + x][j - x] for x in range(4)]) in ["XMAS", "SAMX"]:
            count += 1
        ##part 2 - diag neg
        if i <= len(grid)-3 and j <= len(row)-3 and "".join([grid[i+x][j+x] for x in range(3)]) in ["MAS", "SAM"]:
            #diag pos
            if i <= len(grid) - 3 and "".join([grid[i + x][j+(2-x)] for x in range(3)]) in ["MAS", "SAM"]:
                count_part_two += 1

print("part 1:", count)
print("part 2:", count_part_two)




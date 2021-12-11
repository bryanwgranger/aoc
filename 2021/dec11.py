import numpy as np

with open('dec11.txt') as f:
    lines = [[int(num) for num in t.strip()] for t in f.readlines()]

grid = np.array(lines)

flashes = 0
flash_list = []

for step in range(300):
    daily_flash = []
    grid += 1
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r][c] > 9:
                flash_list.append((r,c))

    while len(flash_list) != 0:
        r, c = flash_list.pop(0)
        if grid[r][c] > 9 and (r,c) not in daily_flash:
            flashes += 1
            daily_flash.append((r,c))
            dr = [-1, -1, -1, 0, 0, 1, 1, 1]
            dc = [-1, 0, 1, -1, 1, -1, 0, 1]
            for i in range(8):
                rr = r + dr[i]
                cc = c + dc[i]
                if 0 <= rr < grid.shape[0] and 0 <= cc < grid.shape[1]:
                    grid[rr][cc] += 1
                    if grid[rr][cc] > 9:
                        flash_list.append((rr,cc))
    for r,c in daily_flash:
        grid[r][c] = 0

    if step == 99:
        pt1_ans = flashes

    if len(daily_flash) == 100:
        pt2_ans = step + 1
        break

print('part 1:')
print(pt1_ans)

print('part 2:')
print(pt2_ans)



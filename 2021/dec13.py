with open('dec13.txt') as f:
    lines = [t.strip() for t in f.readlines()]

points = []
folds = []
for line in lines:
    if line[:4] == 'fold':
        dir = line.split('=')[0][-1]
        mag = int(line.split('=')[1])
        folds.append((dir, mag))
    else:
        if line:
            points.append(line)

x = [int(p.split(',')[0]) for p in points]
y = [int(p.split(',')[1]) for p in points]

grid = []
row = ['.'] * (max(x)+1)

for _ in range(max(y)+1):
    grid.append(['.'] * (max(x)+1))

for i, pt in enumerate(points):

    r = int(pt.split(',')[1])
    c = int(pt.split(',')[0])

    grid[r][c] = '#'

count = 0
for dir, mag in folds:
    if dir == 'y':
        new_grid = []
        for i in range(mag):
            above = i
            below = i + 1
            new_line = []
            for j in range(len(grid[above])):
                if grid[above][j] == '#' or grid[-below][j] == '#':
                    new_line.append('#')
                else:
                    new_line.append('.')
            new_grid.append(new_line)
    else:
        new_grid = []
        for i in range(len(grid)):
            new_line = []
            for j in range(mag):
                left = j
                right = j + 1
                if grid[i][left] == '#' or grid[i][-right] == '#':
                    new_line.append('#')
                else:
                    new_line.append('.')
            new_grid.append(new_line)

    grid = new_grid.copy()

    if count == 0:
        dots = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '#':
                    dots += 1
    count += 1

print('part 1:')
print(dots)
print('part 2:')
for k in range(len(grid)):
    print(grid[k])

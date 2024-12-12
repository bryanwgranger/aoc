with open("dec12.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)

grid = [list(l) for l in lines]
print(grid)
plants = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        plants.append((grid[r][c],r,c))

seen_plants = set()

while plants:
    cur_plant = plants.pop(0)
    print(cur_plant)
    cur_region = set()
    cur_region.add(cur_plant)
    print(cur_region)
    while cur_region:
        p, r, c = cur_region.pop()
        print(r,c)
        neighors = set()
        #above
        if 0 < r:
            if grid[r-1][c] == grid[r][c] and (grid[r-1][c],r-1,c) not in cur_region:
                cur_region.add((grid[r-1][c],r-1,c))
        #below
        if r < len(grid)-1:
            if grid[r+1][c] == grid[r][c] and (grid[r+1][c],r+1,c) not in cur_region:
                cur_region.add((grid[r-1][c],r+1,c))
        #left
        if 0 < c:
            if grid[r][c-1] == grid[r][c] and (grid[r][c-1],r,c-1) not in cur_region:
                cur_region.add((grid[r][c-1],r,c-1))
        #right
        if c < len(grid[0])-1:
            if grid[r][c+1] == grid[r][c] and (grid[r][c+1],r,c+1) not in cur_region:
                cur_region.add((grid[r][c+1],r,c+1))

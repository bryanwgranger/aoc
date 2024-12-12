with open("dec10.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)

grid =[[int(s) for s in l] for l in lines]
print(grid)

d = [(-1,0), #up
     (0,-1), #left
     (1,0), #down
     (0,1), #right
     ]

trailheads = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            trailheads.append((r,c))
print(trailheads)
success = []
while trailheads:
    r,c = trailheads.pop()
    p = 0
    cr = r
    cc = c
    path = True
    print("starting", (cr,cc))
    pathways_to_check = set()
    pathways_to_check.add((cr,cc))
    while p < 9 and pathways_to_check:
        new_r, new_c = pathways_to_check.pop()
        #check above
        print("new_r", new_r)
        if 0 < new_r < len(grid)-1 and grid[new_r-1][new_c] == p + 1:
            print("nailed it")
            pathways_to_check.add((new_r-1,new_c))
            p += 1
        # check below
        elif 0 < new_r < len(grid)-1 and grid[new_r + 1][new_c] == p + 1:
            print("nailed it")
            pathways_to_check.add((new_r + 1, new_c))
            p += 1
        # check left
        elif 0 < new_c < len(grid[0]) - 1 and grid[new_r][new_c - 1] == p + 1:
            print("nailed it")
            pathways_to_check.add((new_r, new_c - 1))
            p += 1
        # check above
        elif 0 < new_c < len(grid[0]) - 1 and grid[new_r - 1][new_c] == p + 1:
            print("nailed it")
            pathways_to_check.add((new_r, new_c + 1))
            p += 1
        else:
            path = False

        #path = False
    if p == 9:
        success.append((r,c))
print(success)
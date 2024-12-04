with open("dec14_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)

grid = []
rock_pos = []
block_pos = []
for j, l in enumerate(lines):
    grid.append(list(l))
    for i, ch in enumerate(l):
        if ch == "O":
            rock_pos.append((i, j))
        elif ch == "#":
            block_pos.append((i,j))

rock_pos = sorted(rock_pos)
print(rock_pos)
print(sorted(block_pos))
from collections import defaultdict
#blocks per column
block_col_dict = defaultdict(list)
for b_x, b_y in sorted(block_pos):
    block_col_dict[b_x].append(b_y)
print(block_col_dict)

def matrix_rotate(ncols, rock_pos):
    new_rock_pos = []
    for r_x, r_y in rock_pos:
        new_rock_pos.append((ncols-r_y-1,r_x))
    return new_rock_pos

def tilt_grid(grid, rock_pos, block_pos, turns=1, rotate=False):

    for u in range(turns):
        block_col_dict = defaultdict(list)
        for b_x, b_y in sorted(block_pos):
            block_col_dict[b_x].append(b_y)
        #print(block_col_dict)

        new_rock_pos = []
        if u == turns-1:
            score = 0
        for c in range(len(grid[0])):

            block_locs = block_col_dict[c]
            # print("COLUMN:", c, "|| BLOCKS:",block_locs)
            top = 0
            mids = {}
            for r_x, r_y in sorted(rock_pos, key=lambda x: x[0]):

                if r_x == c:
                    # print((r_x, r_y))
                    if not block_locs:
                        top += 1
                        continue
                    for i, b_y in enumerate(block_locs):
                        if r_y < b_y:
                            if i == 0:
                                top += 1
                                break
                            else:
                                if block_locs[i-1]+1 not in mids.keys():
                                    mids[block_locs[i-1]+1] = 0
                                mids[block_locs[i-1]+1] += 1
                                break
                        else:
                            if r_y > b_y and b_y == max(block_locs):
                                if max(block_locs)+1 not in mids.keys():
                                    mids[max(block_locs)+1] = 0
                                mids[max(block_locs)+1] += 1
                elif r_x > c:
                    break

            #
            # print("top",top)
            # print("mids", mids)

            #scoring

            for t in range(top):
                if u == turns - 1:
                    score += len(grid)-t
                new_rock_pos.append((c, t))
            for k, v in mids.items():
                for z in range(v):
                    if u == turns - 1:
                        score += len(grid) - (k) - z
                    new_rock_pos.append((c, k+z))

        if rotate:
            rock_pos = matrix_rotate(len(grid[0]), new_rock_pos)
            block_pos = matrix_rotate(len(grid[0]), block_pos)

        if u % 1000 == 0:
            print(u)
    return score

print(tilt_grid(grid, rock_pos, block_pos, turns=1000000000, rotate = True))



assert False



#rocks per column

rock_col_dict = defaultdict(int)
for r_x, r_y in rock_pos:
    rock_col_dict[r_x] += 1

block_rock = defaultdict(list)
for b_x, b_y in sorted(block_pos):
    for r_x, r_y in sorted(rock_pos):
        if r_x == b_x:
            block_rock[(b_x, b_y)].append((r_x,r_y))
            if r_y > b_x:
                print("rock below", b_x, b_y)
print(block_rock)

col_dict = defaultdict(list)
blocked_rocks = []
for k, v in block_rock.items():
    b_x, b_y = k
    top = []
    for r_x, r_y in v:
        if r_y < b_y:
            top[r_x] +=1
        else:
            blocked_rocks.append((r_x, ))




assert False
def tilt_grid(grid):
    for r in range(len(grid)):
        for p in range(len(grid[r])):
            if r == 0:
                continue
            if grid[r][p] == "O":
                j = 0
                above_char = grid[r-(j+1)][p]
                if above_char == ".":
                    while above_char not in ["O", "#"] and r > j:
                        j += 1
                        above_char = grid[r-(j+1)][p]
                    grid[r-j][p] = "O"
                    grid[r][p] = "."

    return grid

def score_grid(grid):
    score = 0
    for i, r in enumerate(grid):
        for p in r:
            if p == "O":
                score += len(grid)-i
    return score

print("answer part one:", score_grid(tilt_grid(grid)))


test_grid = [[1,2,3], [4,5,6], [7,8,9]]
def rotate_grid(grid):
    new_grid = []
    for c in range(len(grid[0])):
        new_row = []
        for r in range(len(grid)-1, -1, -1):
            new_row.append(grid[r][c])
        new_grid.append(new_row)
    return new_grid

print(rotate_grid(test_grid))


for i in range(1000000000):
    grid = rotate_grid(grid)
    if i % 1000 == 0:
        print(i)

print(score_grid(grid))

assert False
output_ex = ""
for i in range(10):
    for j in range(10):
        if (j,i) in rock_pos:
            output_ex += "O"
        else:
            output_ex += "."
    output_ex += "\n"
print(output_ex)

assert False


rock_pos = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'O':
            rock_pos.append((c,r))

print(rock_pos)
print(len(rock_pos))
new_rock_pos = []
for rock_x, rock_y in sorted(rock_pos, key=lambda x: x[1]):
    print(rock_y)
    if rock_y > 0:
        i = 1
        above_char = grid[rock_y-i][rock_x]
        while above_char not in ["#", "O"] and rock_y-i > 0:
            i += 1
            above_char = grid[rock_y - i][rock_x]
        new_rock_pos.append((rock_x, rock_y-i))
    else:
        new_rock_pos.append((rock_x, rock_y))

print(new_rock_pos)
print(len(new_rock_pos))
score = 0
from collections import Counter
c = Counter([r[1] for r in new_rock_pos])
print(c)
for k,v in c.items():
    score += v * (len(grid)-k)

print(score)

output_ex = ""
for i in range(10):
    for j in range(10):
        if (j,i) in new_rock_pos:
            output_ex += "O"
        else:
            output_ex += "."
    output_ex += "\n"
print(output_ex)
#with open("dec14_viz.ex", "w") as outfile:



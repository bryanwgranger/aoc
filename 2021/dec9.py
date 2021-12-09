with open('dec9.txt') as f:
    lines = [t.strip() for t in f.readlines()]

low_points = []
coords = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if i != 0 and i != len(lines)-1:
            if j != 0 and j != len(lines[0])-1:

                if int(lines[i][j]) < int(lines[i-1][j-1]) and \
                    int(lines[i][j]) < int(lines[i-1][j]) and \
                    int(lines[i][j]) < int(lines[i-1][j+1]) and \
                    int(lines[i][j]) < int(lines[i][j-1]) and \
                    int(lines[i][j]) < int(lines[i][j+1]) and \
                    int(lines[i][j]) < int(lines[i+1][j-1]) and \
                    int(lines[i][j]) < int(lines[i+1][j]) and \
                    int(lines[i][j]) < int(lines[i+1][j+1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))
            elif j == 0:
                if int(lines[i][j]) < int(lines[i-1][j]) and \
                    int(lines[i][j]) < int(lines[i-1][j+1]) and \
                    int(lines[i][j]) < int(lines[i][j+1]) and \
                    int(lines[i][j]) < int(lines[i+1][j]) and \
                    int(lines[i][j]) < int(lines[i+1][j+1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))

            else:
                if int(lines[i][j]) < int(lines[i-1][j-1]) and \
                    int(lines[i][j]) < int(lines[i-1][j]) and \
                    int(lines[i][j]) < int(lines[i][j-1]) and \
                    int(lines[i][j]) < int(lines[i+1][j-1]) and \
                    int(lines[i][j]) < int(lines[i+1][j]):
                        low_points.append(int(lines[i][j]))
                        coords.append((i,j))


        elif i == 0:
            if j != 0 and j != len(lines[0])-1:

                if  int(lines[i][j]) < int(lines[i][j-1]) and \
                        int(lines[i][j]) < int(lines[i][j+1]) and \
                        int(lines[i][j]) < int(lines[i+1][j-1]) and \
                        int(lines[i][j]) < int(lines[i+1][j]) and \
                        int(lines[i][j]) < int(lines[i+1][j+1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))

            elif j == 0:
                if int(lines[i][j]) < int(lines[i][j+1]) and \
                        int(lines[i][j]) < int(lines[i+1][j]) and \
                        int(lines[i][j]) < int(lines[i+1][j+1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))

            else:
                if int(lines[i][j]) < int(lines[i][j-1]) and \
                        int(lines[i][j]) < int(lines[i+1][j-1]) and \
                        int(lines[i][j]) < int(lines[i+1][j]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))
        else:
            if j != 0 and j != len(lines[0])-1:

                if int(lines[i][j]) < int(lines[i-1][j-1]) and \
                        int(lines[i][j]) < int(lines[i-1][j]) and \
                        int(lines[i][j]) < int(lines[i-1][j+1]) and \
                        int(lines[i][j]) < int(lines[i][j-1]) and \
                        int(lines[i][j]) < int(lines[i][j+1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))

            elif j == 0:
                if int(lines[i][j]) < int(lines[i-1][j]) and \
                        int(lines[i][j]) < int(lines[i-1][j+1]) and \
                        int(lines[i][j]) < int(lines[i][j+1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))

            else:
                if int(lines[i][j]) < int(lines[i-1][j-1]) and \
                        int(lines[i][j]) < int(lines[i-1][j]) and \
                        int(lines[i][j]) < int(lines[i][j-1]):
                            low_points.append(int(lines[i][j]))
                            coords.append((i,j))


print('part 1:')
print(sum(low_points)+len(low_points))


def top(orig, r, c):
    return orig < int(lines[r-1][c])

def left(orig, r, c):
    return orig < int(lines[r][c-1])

def right(orig, r, c):
    return orig < int(lines[r][c+1])

def bottom(orig, r, c):
    return orig < int(lines[r+1][c])


def check_adj(pt):
    r = pt[0]
    c = pt[1]
    orig = int(lines[r][c])

    rtn_pts = []
    if r != 0 and r != len(lines)-1:
        if c != 0 and c != len(lines[0])-1:
            #top
            if top(orig, r, c):
                rtn_pts.append((r-1, c))
            #left
            if left(orig, r, c):
                rtn_pts.append((r, c-1))
            #right
            if right(orig, r, c):
                rtn_pts.append((r, c+1))
            #bottom
            if bottom(orig, r, c):
                rtn_pts.append((r+1, c))
        elif c == 0:
            #top
            if top(orig, r, c):
                rtn_pts.append((r-1, c))
            #right
            if right(orig, r, c):
                rtn_pts.append((r, c+1))
            #bottom
            if bottom(orig, r, c):
                rtn_pts.append((r+1, c))

        else: # right most column
            #top
            if top(orig, r, c):
                rtn_pts.append((r-1, c))
            #left
            if left(orig, r, c):
                rtn_pts.append((r, c-1))
            #bottom
            if bottom(orig, r, c):
                rtn_pts.append((r+1, c))
    elif r == 0:
        if c != 0 and c != len(lines[0])-1:

            #left
            if left(orig, r, c):
                rtn_pts.append((r, c-1))
            #right
            if right(orig, r, c):
                rtn_pts.append((r, c+1))
            #bottom
            if bottom(orig, r, c):
                rtn_pts.append((r+1, c))
        elif c == 0:

            #right
            if right(orig, r, c):
                rtn_pts.append((r, c+1))
            #bottom
            if bottom(orig, r, c):
                rtn_pts.append((r+1, c))

        else: # right most column
            #top

            #left
            if left(orig, r, c):
                rtn_pts.append((r, c-1))
            #bottom
            if bottom(orig, r, c):
                rtn_pts.append((r+1, c))

    else: #bottom row
        if c != 0 and c != len(lines[0])-1:
            #top
            if top(orig, r, c):
                rtn_pts.append((r-1, c))
            #left
            if left(orig, r, c):
                rtn_pts.append((r, c-1))
            #right
            if right(orig, r, c):
                rtn_pts.append((r, c+1))

        elif c == 0:
            #top
            if top(orig, r, c):
                rtn_pts.append((r-1, c))
            #right
            if right(orig, r, c):
                rtn_pts.append((r, c+1))

        else: # right most column
            #top
            if top(orig, r, c):
                rtn_pts.append((r-1, c))
            #left
            if left(orig, r, c):
                rtn_pts.append((r, c-1))
    return rtn_pts

new_points = []
basins = {}


used_points = []
for pt in coords:
    working_points = []

    basins[pt] = 1
    new = check_adj(pt)
    used_points.append(pt)
    for n in new:
        working_points.append(n)
    while len(working_points) != 0:
        for i, p in enumerate(working_points):
            if p not in used_points and int(lines[p[0]][p[1]]) != 9:

                basins[pt] += 1
                newer = check_adj(p)
                for n in newer:
                    working_points.append(n)

                used_points.append(p)
            working_points.pop(working_points.index(p))

final = sorted(basins.items(), key= lambda item: item[1], reverse=True)

ans = 1
for i in range(3):
    ans *= final[i][1]
print('part 2:')
print(ans)

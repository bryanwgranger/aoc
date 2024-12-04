with open("dec10_2023.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)
mat = []

valid_con = {(0,-1): ["F","|", "7"], #above
             (0,1): ["|", "L" ,"J"], #below
             (1,0): ["J","-", "7"], #right
             (-1,0): ["-", "L" ,"F"], #left
             }

directions = list(valid_con.keys())
connections = {
    "|": {(0,-1): ["F","|", "7"], (0,1): ["|", "L" ,"J"]},
    "-": {(1,0): ["J","-", "7"], (-1,0): ["-", "L" ,"F"]},
    "F": {(1,0): ["J","-", "7"], (0,1): ["-", "L" ,"F"]},
    "J": {(-1,0): ["F","-", "L"], (0,-1): ["F","|", "7"]},
    "L": {(1,0): ["J","-", "7"], (0,-1): ["F","|", "7"]},
    "7": {(-1,0): ["F","-", "L"], (0,1): ["-", "L" ,"F"]},

}
start_point = None
for i,l in enumerate(lines):
    for j,k in enumerate(l):
        if k == "S":
            start_point = (j,i)
            break
    if start_point:
        break

print(start_point)
path_points = []
seen_points = [start_point]
cur_point = start_point
sp_j, sp_i = start_point
#determine start point p
possible_S = []
for pt, chars in valid_con.items():
    g, h = pt
    new_char = lines[sp_i + h][sp_j + g]
    if new_char in chars:
        pass
assert False

print("cur point", cur_point)
start = True
for _ in range(7):
    print("+"*60)
    print(cur_point)
    s_j, s_i = cur_point
    con_list = []
    for pt, chars in valid_con.items():
        g, h = pt
        # print(pt)
        # print(lines[s_i+h][s_j+g])
        cur_char = lines[s_i][s_j]
        new_char = lines[s_i+h][s_j+g]
        if (s_j+g, s_i+h) in seen_points:
            continue
        if new_char in chars:
            if new_char in connections[cur_char]:
            # print('yes')
            # print("S", lines[s_i][s_j])
                print('valid ch', lines[s_i+h][s_j+g])
                print(f"{cur_point} -> {(s_j+g, s_i+h)}")
            #con_list.append((s_j+g, s_i+h))
            #print('yes', lines[s_i+g][s_j+h])

                seen_points.append((s_j+g, s_i+h))
                cur_point = (s_j+g, s_i+h)
                if cur_point == start_point:
                    print("break")
                    break

    #print(con_list)
    print(seen_points)
assert False
#assert len(con_list) == 1
print('len 2')
if cur_point == start_point and start:
    seen_points.append(con_list[0])
    cur_point = con_list[1]
    start = False
else:
# cur_point = con_list[1]
    for p in con_list:
        if p not in seen_points:
            seen_points.append(p)
            cur_point = p
# if cur_point == start_point:
#     break
print(seen_points)


assert False
path_points = []

new_point = start_point

while True:
    pass
    #start with a point - find which connections it may have





for i, y in enumerate(lines):
    for j, x in enumerate(y):
        coord = (j,i)
        ch = lines[i][j]
        if ch == ".":
            continue
        if ch == "S":
            path_points.append(coord)
            continue
        con_list = []

        #edge invalids "J" on top row e.g.
        if j == len(y) - 1:
            if ch in ["-", "F", "L"]:
                continue
        elif j == 0:
            if ch in ["-", "7", "J"]:
                continue
        elif i == 0:
            if ch in ["|", "L", "J"]:
                continue
        elif i == len(lines) - 1:
            if ch in ["|", "7", "F"]:
                continue

        for comp_pos, poss_ch in connections[ch]:
            # print(ch, comp_pos, poss_ch)
            # print(comp_pos)
            # print(comp_pos[0])
            #for pt in comp_pos:
            g = comp_pos[0]
            h = comp_pos[1]
            if j == len(y)-1 and g == 1:
                continue
            elif j == 0 and g == -1:
                continue
            elif i == 0 and h == -1:
                continue
            elif i == len(lines)-1 and h == 1:
                continue
            compare_ch = lines[j+g][i+h]
            if compare_ch in poss_ch:
                con_list.append((j+g,i+h))
                #print(coord, ch, con_list)
        if len(con_list) == 2:
            path_points.extend(con_list)
            print(ch, coord, con_list)
#
#
path_points = set(path_points)
print(len(set(path_points)))
print(len(set(path_points)) / 2)

def distance(a,b):
    return ((a[1] - b[1]) ** 2 + (a[0] - b[0]) ** 2) ** 1/2

print(distance((0,0), (1,0)))
print(distance((0,0), (1,1)))
contig = []
# for p in path_points:
#     for q in path_points:
#         if distance(p,q) <= 0.5 and p not in contig:
#             contig.append(p)
#
#
# print(contig)
#
# print(len(contig))
#
# import plotly.graph_objs as go
# fig = go.Figure(go.Scatter(
#         x=[r[0] for r in contig],
#         y=[d[1] for d in contig],
#         mode="markers",
# ))
#
# fig.show()

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
m = np.zeros((len(lines[0]), len(lines)))
for c in path_points:
    m[c[0],c[1]] = 1
print(m)
g = sns.heatmap(m)
plt.show()
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
    "|": [((0,-1), ["F","|", "7"]), ((0,1), ["|", "L" ,"J"])],
    "-": [((1,0), ["J","-", "7"]), ((-1,0), ["-", "L" ,"F"])],
    "F": [((1,0), ["J","-", "7"]), ((0,1), ["-", "L" ,"F"])],
    "J": [((-1,0), ["F","-", "L"]), ((0,-1), ["F","|", "7"])],
    "L": [((1,0), ["J","-", "7"]), ((0,-1), ["F","|", "7"])],
    "7": [((-1,0), ["F","-", "L"]),((0,1), ["-", "L" ,"F"])],

}
start_point = None
for i,l in enumerate(lines):
    for j,k in enumerate(l):
        if k == "S":
            print("double found")
            start_point = (j,i)
            break
    if start_point:
        break

path_points = []

new_point = start_point
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
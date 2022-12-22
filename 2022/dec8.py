import numpy as np
from collections import defaultdict

with open('dec8ex.txt', 'r') as f:
    lines = [[int(a) for a in t.strip()] for t in f.readlines()]

vis = 99 + 99 + 97 + 97

#from top
top_vis_count = 99
top_vis_idx = list(range(len(lines[0])))
tree_dict = {e: 1 for e in list(range(len(lines[0])))}
bottom_tree_dict = {g: 1 for g in range(len(lines[0]))}
print(tree_dict)

#top
vis_trees = [(0, s) for s in range(len(lines[0]))]
cols = [p[1] for p in vis_trees]
r = 0
while cols:
    to_remove = []
    for i in cols:

        if lines[r+1][i] > lines[r][i]:
            vis_trees.append((r, i))
        else:
            to_remove.append(i)
    cols = [h for h in cols if h not in to_remove]
    r += 1
#bottom
vis_trees.extend([(len(lines[0])-1, s) for s in range(len(lines[0]))])
cols = list(range(len(lines[-1])))
r = len(lines[0])-1
while cols:
    to_remove = []
    for i in cols:

        if lines[r-1][i] > lines[r][i]:
            vis_trees.append((r, i))
        else:
            to_remove.append(i)
    cols = [h for h in cols if h not in to_remove]
    r -= 1

#left
vis_trees.extend([(s, 0) for s in range(len(lines[0]))])
rows = list(range(len(lines)))
c = 0
while rows:
    to_remove = []
    for i in rows:

        if lines[c+1][i] > lines[c][i]:
            vis_trees.append((c, i))
        else:
            to_remove.append(i)
    rows = [h for h in rows if h not in to_remove]
    c += 1

#right
vis_trees.extend([(s, len(lines[0])-1) for s in range(len(lines[0]))])
rows = list(range(len(lines)))
c = len(lines[0])-1
while rows:
    to_remove = []
    for i in rows:

        if lines[c - 1][i] > lines[c][i]:
            vis_trees.append((c, i))
        else:
            to_remove.append(i)
    rows = [h for h in rows if h not in to_remove]
    c -= 1

print(len(vis_trees))
print(vis_trees)
print(len(set(vis_trees)))
print(set(vis_trees))

with open("dec17_2023.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)

grid = []
for l in lines:
    grid.append(list(l))

directions = {(0,-1): "above", #above
              (1,0): "right", #right
              (0,1): "below", #below
              (-1,0): "left" #left
              }

directions_lim = {
              (1,0): "right", #right
              (0,1): "below", #below
              (0,-1): "above", #above
        }

seen_points = []
grid_r = len(grid) - 1
grid_c = len(grid[0]) - 1
start_point = (0,0)
end_point = (grid_r, grid_c)
print(end_point)
pt = start_point
seen_points.append(pt)
print()
print("START\n")

dir_hist = []
total = 0
while end_point not in seen_points:
    neighbors = []
    grid_vals = []

    for i,j in directions_lim.keys():
        if 0 <= pt[0] + i <= grid_r and 0 <= pt[1] + j <= grid_c:
            if (pt[0]+i, pt[1]+j) not in seen_points:
                neighbors.append(((pt[0]+i, pt[1]+j), directions_lim[(i,j)]))
                grid_vals.append(int(grid[pt[0]+i][pt[1]+j]))

    print(seen_points)
    print(pt, "-> neighbors", neighbors, "-> grid_vals", grid_vals)
    if len(set(dir_hist[-3:])) == 1:
        no_dir = dir_hist[-1]

        for n, neigh in enumerate(neighbors):
            if neigh[1] == no_dir:
                neighbors.pop(n)
                grid_vals.pop(n)


    new_pt_idx = grid_vals.index(min(grid_vals))
    total += min(grid_vals)
    print(new_pt_idx)
    new_point, dir = neighbors[new_pt_idx]
    print(new_point)
    print(dir)
    dir_hist.append(dir)
    print(dir_hist[-3:])
    #print(new_point)
    seen_points.append(new_point)
    pt = new_point

print(len(seen_points))
print(total)
import plotly.graph_objs as go
fig = go.Figure(go.Scatter(
    x=[s[1] for s in seen_points],
    y=[s[0] for s in seen_points],
    mode="markers"
))
#fig.show()
with open('dec5.txt') as f:
    n = list(num.strip() for num in f.readlines())
    coords = []
    horizontal = []
    vertical = []
    diagonal = []
    for pair in n:
        c = pair.split( " -> ")
        coords.append(c)
        if c[0].split(',')[0] == c[1].split(',')[0]:
            horizontal.append(c)
        elif c[0].split(',')[1] == c[1].split(',')[1]:
            vertical.append(c)
        else:
            diagonal.append(c)


all_points = []
pt1_points = []
for pair in horizontal:
    x1 = int(pair[0].split(',')[0])
    x2 = int(pair[1].split(',')[0])
    y1 = int(pair[0].split(',')[1])
    y2 = int(pair[1].split(',')[1])

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            pt1_points.append(f'{x1},{i}')
            all_points.append(f'{x1},{i}')

for pair in vertical:
    x1 = int(pair[0].split(',')[0])
    x2 = int(pair[1].split(',')[0])
    y1 = int(pair[0].split(',')[1])
    y2 = int(pair[1].split(',')[1])

    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
            pt1_points.append(f'{i},{y1}')
            all_points.append(f'{i},{y1}')

for pair in diagonal:
    x1 = int(pair[0].split(',')[0])
    x2 = int(pair[1].split(',')[0])
    y1 = int(pair[0].split(',')[1])
    y2 = int(pair[1].split(',')[1])

    if x1 < x2:
        x_range = [x for x in range(x1, x2+1)]
    else:
        x_range = [x for x in range(x1, x2-1, -1)]
    if y1 < y2:
        y_range = [y for y in range(y1, y2+1)]
    else:
        y_range = [y for y in range(y1, y2-1, -1)]

    diags = list(zip(x_range, y_range))

    for d in diags:
        all_points.append(f'{d[0]},{d[1]}')

pt1_results = []
pt2_results = []
count_dict_pt1 = {}
count_dict_pt2 = {}

#part 1
for point in pt1_points:
    if point not in count_dict_pt1.keys():
        count_dict_pt1[point] = 1
    else:
        count_dict_pt1[point] += 1

for k, v in count_dict_pt1.items():
    if v >= 2:
        pt1_results.append(k)

#part 2
for point in all_points:
    if point not in count_dict_pt2.keys():
        count_dict_pt2[point] = 1
    else:
        count_dict_pt2[point] += 1

for k, v in count_dict_pt2.items():
    if v >= 2:
        pt2_results.append(k)

print('part 1:')
print(len(pt1_results))

print('part 2:')
print(len(pt2_results))









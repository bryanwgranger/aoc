import numpy as np

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


# print(horizontal)
all_points = []
for pair in horizontal:
    x1 = int(pair[0].split(',')[0])
    x2 = int(pair[1].split(',')[0])
    y1 = int(pair[0].split(',')[1])
    y2 = int(pair[1].split(',')[1])

    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            all_points.append(f'{x1},{i}')

for pair in vertical:
    x1 = int(pair[0].split(',')[0])
    x2 = int(pair[1].split(',')[0])
    y1 = int(pair[0].split(',')[1])
    y2 = int(pair[1].split(',')[1])

    if y1 == y2:
        for i in range(min(x1, x2), max(x1, x2)+1):
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
    print(x_range)
    print(y_range)

    diags = list(zip(x_range, y_range))

    for d in diags:
        all_points.append(f'{d[0]},{d[1]}')

print(len(all_points))

double_list = []
count_dict = {}

for point in all_points:
    if point not in count_dict.keys():
        count_dict[point] = 1
    else:
        count_dict[point] += 1

for k, v in count_dict.items():
    if v >= 2:
        double_list.append(k)

print('part 1:')
print(len(double_list))







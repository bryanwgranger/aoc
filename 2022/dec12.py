with open('dec12ex.txt') as f:
    lines = [[a for a in t.strip()] for t in f.readlines()]

print(lines)
DR = {"U": -1, 'D':1, "L":0, "R":0}
DC = {"U": 0, 'D':0, "L":-1, "R":1}

def find_heights(point):
    p = lines[point[0]][point[1]]
    #dir = ['U', 'D', 'L', 'R']
    diffs = {}
    for d in DR.keys():
        try:
            comp_point = (point[0] + DR[d], point[1] + DC[d])
            if comp_point[0] < 0 or comp_point[1] < 0:
                continue
            new_p = lines[comp_point[0]][comp_point[1]]
            if (delta := ord(new_p)-ord(p)) > -1:
                diffs[d] = delta

        except:
            pass
    return sorted([(k,v) for k,v in diffs.items()], key = lambda x: x[1], reverse=True)

print(find_heights((0,0)))

start = (0,0)

for i, r in enumerate(lines):
    if 'E' in r:
        end_point = (i, r.index('E'))

current_point = start
pt_history = set()
pt_history.add(current_point)
prev_point = start
#
while current_point != end_point:
    diffs = find_heights(current_point)
    print(diffs)
    direction = diffs[0][0]
    next_point = (current_point[0] + DR[direction], current_point[1] + DC[direction])
    try:
        if next_point == prev_point:
            direction = diffs[1][0]
            next_point = (current_point[0] + DR[direction], current_point[1] + DC[direction])
    except:
        pass
    print(next_point)
    print(lines[next_point[0]][next_point[1]])
    prev_point = current_point
    current_point = next_point
    pt_history.add(current_point)

print(len(pt_history))
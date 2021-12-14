import numpy as np
from collections import deque

with open('dec12ex.txt') as f:
    lines = [t.strip() for t in f.readlines()]

print(lines)

caves = []
connections ={}
for c in lines:
    cc = c.split('-')
    for cave in cc:
        if cave not in caves:
            caves.append(cave)
    if cc[0] not in connections.keys():
        connections[cc[0]] = [cc[1]]
    else:
        connections[cc[0]].append(cc[1])
    if cc[1] not in connections.keys():
        connections[cc[1]] = [cc[0]]
    else:
        connections[cc[1]].append(cc[0])
print(connections)
print([g for g in connections['HN']])
routes = []

start = ('start', set(['start']))
cave_list = deque([start])

print(cave_list)

sum = 0
while cave_list:
    cave, lc_list = cave_list.popleft()
    for new_cave in connections[cave]:
        if new_cave.islower():
            if new_cave == 'end':
                sum += 1
                continue
            if new_cave not in lc_list and new_cave != 'end':
                lc_list.add(new_cave)
                cave_list.append((new_cave, lc_list))
        else:
            cave_list.append((new_cave, lc_list))
        print(cave_list)
print(sum)



# cave_list = deque([start])
# for con in connections['start']:
#     new_route = ['start']
#
#     new_route.append(con)
#
#     for new_cave in connections['con']:
#         new_route.append(new_cave)
#     next_cave_list = []
#     while new_route[-1] != 'end' and next_cave_list:
#
#         print(len(next_cave_list))
#         next_cave = next_cave_list.pop()
#
#         if next_cave != 'end' and next_cave.islower():
#             if next_cave not in new_route:
#                 new_route.append(next_cave)
#                 for c in connections[next_cave]:
#                     if c not in next_cave_list:
#                         next_cave_list.append(c)
#                 # next_cave_list.extend(connections[next_cave])
#         else:
#             new_route.append(next_cave)
#             for c in connections[next_cave]:
#                 if c not in next_cave_list:
#                     next_cave_list.append(c)
#         print(next_cave_list)
#         print(new_route)
#
#
#
#
#
#
#


def find_route(cave):
    new_route = []
    new_route.append(cave)
    all_routes = []
    lc_seen = []
    for next_cave in connections[cave]:
        new_route.append(cave)
        end = False
        while next_cave is not 'end':
        #check if lowercase and hasn't been visited
            if next_cave.islower() and len(next_cave) != 2 and next_cave not in new_route and next_cave != 'end':
                new_route.append(next_cave)
                for next_next_cave in connections[next_cave]:
                    pass

            elif next_cave == 'end':
                new_route.append(next_cave)
                all_routes.append(new_route)
                end = True
                # return new_route
            # else:
            #     new_route.append(next_cave)
        all_routes.append(new_route)

# print(find_route('HN'))
# for con in connections['start']:
#     end = False
#     # to_explore =[]
#     next_cave = con
#     # print(to_explore)
#     lc_seen = []
#     for next_next_cave in connections[next_cave]:
#         new_route = ['start', next_cave]
#         if next_next_cave.islower() and len(next_next_cave) != 2 and next_next_cave not in new_route:
#             lc_seen.append(next_next_cave)
#
#     new_route = []




#
#
#
#     while not end:
#         new_route.append('start')
#
#         exploring_pt = next_cave
#
#         for newer_cave in connections[next_cave]:
#
#
#             lc_seen = []
#
#
#             for cv in connections[con]:
#
#             # to_explore.append(cv)
#             # for cvv in connections[cv]:
#             #     to_explore.append(cvv)
#
#             # print(to_explore)
#
#             if new_route[-1] != cv and cv not in lc_seen:
#                 new_route.append(cv)
#                 # to_explore.pop(to_explore.index(cv))
#             if cv.islower() and cv not in ['start', 'end']:
#                 lc_seen.append(cv)
#             if cv == 'end':
#                 routes.append(new_route)
#                 end = True
#
#
# print(routes)
# print(len(routes))

# print(caves)
# cave_to_id = {}
# id_to_cave = {}
# for i in range(len(caves)):
#     cave_to_id[caves[i]] = i
#     id_to_cave[i] = caves[i]
#
# graph = np.zeros((len(caves), len(caves)))
#
# for route in lines:
#     s, t = route.split('-')
#     graph[cave_to_id[s]][cave_to_id[t]] += 1
#
# print(graph)

routes = []





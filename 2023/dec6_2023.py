with open("dec6_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

times = [int(y.strip()) for y in lines[0].split(":")[-1].split()]
distances = [int(d.strip()) for d in lines[1].split(":")[-1].split()]

ways_to_win = {k:0 for k in times}
for time, distance in zip(times, distances):
    speed = 0
    for t in range(time):
        button_hold = t
        d_traveled = (time - t) * t
        if d_traveled > distance:
            ways_to_win[time] += 1

answer = 1
for v in ways_to_win.values():
    answer *= v
print("answer part one:", answer)

new_time = int("".join([str(s) for s in times]))
new_distance = int("".join([str(d) for d in distances]))

import numpy as np

x = np.linspace(0,new_time,new_time+1)
y = (new_time - x) * x - new_distance

part_two = np.sum(y > 0)

print("answer part two:", part_two)
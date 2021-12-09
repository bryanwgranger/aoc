import numpy as np

with open('dec2.txt') as f:
    n = np.array(list(num.strip() for num in f.readlines()))

horizontal = 0
depth = 0

for move in n:
    direction = move.split()[0]
    value = int(move.split()[1])

    if direction == 'forward':
        horizontal += value
    elif direction == 'down':
        depth += value
    elif direction == 'up':
        depth -= value


print('part 1:')

print(horizontal * depth)

#part 2

horizontal = 0
depth = 0
aim = 0

for move in n:
    direction = move.split()[0]
    value = int(move.split()[1])

    if direction == 'forward':
        horizontal += value
        depth += aim * value
    elif direction == 'down':
        aim += value
    elif direction == 'up':
        aim -= value


print('part 2:')

print(horizontal * depth)

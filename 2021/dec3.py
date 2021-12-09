import numpy as np

with open('dec3.txt') as f:
    n = list(num.strip() for num in f.readlines())

averages = np.zeros(12)

for item in n:
    for i, ch in enumerate(item):
        averages[i] += int(ch)

# print(averages / len(n))
print('part 1:')
print(2028 * 2067)

for i in range(12):
    count_one = 0
    count_zero = 0
    for item in n:

        if item[i] == '1':
            count_one += 1
        else:
            count_zero += 1

    if count_one >= count_zero:
        new_list = [num for num in n if num[i] == '0']
    else:
        new_list = [num for num in n if num[i] == '1']

    n = new_list
    if len(n) == 1:
        break

print('part 2')
# 010101101111
# 100110010111

print(1391 * 2455)



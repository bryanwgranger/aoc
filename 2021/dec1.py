import numpy as np
import pandas as pd

#dec 1 - part 1
with open('dec1.txt') as f:
    n = np.array(list(int(num.strip()) for num in f.readlines()))

print(n)
print(n.shape)

count = 0
for i in range(1, len(n)):
    if n[i] > n[i-1]:
        count += 1
print(count)

#dec1 - part 2

count_part_two = 0
for i in range(1, len(n)-2):
    if (n[i] + n[i+1] + n[i+2]) > (n[i-1] + n[i] + n[i+1]):
        count_part_two += 1
print(count_part_two)

import requests

input_file = 'dec1.txt'

with open(input_file, "r") as f:
    lines = f.readlines()

elf_dict = {}
elf_idx = 1
cals = 0
for l in lines:
    if l == '\n':
        elf_dict[elf_idx] = cals
        elf_idx += 1
        cals = 0
        continue
    cals += int(l)

sorted_dict = {k:v for k,v in sorted(elf_dict.items(), key = lambda x: x[1], reverse=True)}

print(sorted_dict)

print('answer 1: ', list(sorted_dict.values())[0])

print("answer 2:", sum(list(sorted_dict.values())[0:3]))
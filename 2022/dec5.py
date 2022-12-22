from collections import defaultdict

with open('dec5.txt', 'r') as f:
    lines = f.readlines()

print(lines)

the_dict = defaultdict(list)
new_dict = {}
answer_two_dict = {}

#set up the dict
for l in lines[:8]:
    for i in range(0,len(l), 4):
        row = int((i+4)/4)
        val = l[i:i+4]
        print(f"{int((i+4)/4)}:",val)
        if val.startswith("["):
            the_dict[row].append(val[1])
for k, v in the_dict.items():
    new_dict[k] = list(reversed(v))
    answer_two_dict[k] = list(reversed(v))

for l in lines[10:]:
    quantity = int((l.split(' from ')[0]).split()[-1])
    prev = int((l.split(' from ')[-1]).split("to")[0])
    new = int((l.split(' from ')[-1]).split("to")[1])

    for q in range(quantity):
        crate = new_dict[prev].pop(-1)
        new_dict[new].append(crate)

    #part 2
    crates = answer_two_dict[prev][-quantity:]
    answer_two_dict[prev] = answer_two_dict[prev][:-quantity]
    answer_two_dict[new].extend(crates)




answer_one = ""
answer_two = ""
for h in range(1,10):
    answer_one += new_dict[h][-1]
    if answer_two_dict[h]:
        answer_two += answer_two_dict[h][-1]


#part 2



print('answer 1:', answer_one)
print('answer 2:', answer_two)

print(new_dict[2])
print(new_dict[2][-5:])
print(new_dict[2][:-5])
crates = new_dict[2][-5:]
print(new_dict[6])
new_dict[6].extend(crates)
print(new_dict[6])
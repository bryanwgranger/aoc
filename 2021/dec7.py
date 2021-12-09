with open('dec7.txt') as f:
    positions = [int(x) for x in f.read().split(',')]

print(positions)
print(len(positions))

test = [16,1,2,0,4,2,7,1,2,14]


fuel_dict_pt_1 = {}
for pos in positions:
    fuel = 0
    for j in range(len(positions)):
        fuel += abs(pos - positions[j])
    fuel_dict_pt_1[pos] = fuel

print(fuel_dict_pt_1)
print(sorted(fuel_dict_pt_1.items(), key=lambda item: item[1])[0])


fuel_dict_pt_2 = {}

for l in range(len(positions)):
    fuel = 0
    for pos in positions:
        steps = list(range(1, abs(pos-l)+1))
        sum = 0
        for num in steps:
            sum += num
        fuel += sum
    fuel_dict_pt_2[l] = fuel

print(fuel_dict_pt_2)
print(sorted(fuel_dict_pt_2.items(), key=lambda item: item[1])[0])
initial = [3,3,2,1,4,1,1,2,3,1,1,2,1,2,1,1,1,1,1,1,4,1,1,5,2,1,1,2,1,
           1,1,3,5,1,5,5,1,1,1,1,3,1,1,3,2,1,1,1,1,1,1,4,1,1,1,1,1,1,
           1,4,1,3,3,1,1,3,1,3,1,2,1,3,1,1,4,1,2,4,4,5,1,1,1,1,1,1,4,
           1,5,1,1,5,1,1,3,3,1,3,2,5,2,4,1,4,1,2,4,5,1,1,5,1,1,1,4,1,
           1,5,2,1,1,5,1,1,1,5,1,1,1,1,1,3,1,5,3,2,1,1,2,2,1,2,1,1,5,
           1,1,4,5,1,4,3,1,1,1,1,1,1,5,1,1,1,5,2,1,1,1,5,1,1,1,4,4,2,
           1,1,1,1,1,1,1,3,1,1,4,4,1,4,1,1,5,3,1,1,1,5,2,2,4,2,1,1,3,
           1,5,5,1,1,1,4,1,5,1,1,1,4,3,3,3,1,3,1,5,1,4,2,1,1,5,1,1,1,
           5,5,1,1,2,1,1,1,3,1,1,1,2,3,1,2,2,3,1,3,1,1,4,1,1,2,1,1,1,
           1,3,5,1,1,2,1,1,1,4,1,1,1,1,1,2,4,1,1,5,3,1,1,1,2,2,2,1,5,
           1,3,5,3,1,1,4,1,1,4]

test = [3,4,3,1,2]


new_population = initial
days1 = 80


for i in range(days1):
    newer_population = []
    count = 0
    for num in new_population:
        if num > 0:
            new_num = num - 1
            newer_population.append(new_num)
        else:
            new_num = 6
            newer_population.append(new_num)
            count += 1
    for j in range(count):
        newer_population.append(8)
    new_population = newer_population

print('part 1:')
print(len(new_population))


#for part 2

days2 = 256

new_fish_dict = {k:0 for k in range(256)}

daily_fish_dict = {k:0 for k in range(9)}

for num in initial:
    daily_fish_dict[num] += 1

for i in range(days2):
    t_dict = {k:0 for k in range(9)}
    for j in range(9):
        if j == 0:
            t_dict[6] = daily_fish_dict[0]
            t_dict[8] = daily_fish_dict[0]
        else:
            t_dict[j-1] += daily_fish_dict[j]
    daily_fish_dict = t_dict

total_sum = 0
for k, v in daily_fish_dict.items():
    total_sum += v
print('part 2:')
print(total_sum)






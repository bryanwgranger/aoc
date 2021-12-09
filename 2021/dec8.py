with open('dec8.txt') as f:
    lines = [t.strip() for t in f.readlines()]

counter = {1: 0,
           4: 0,
           7: 0,
           8: 0,}

decoder = {2: 1,
           4: 4,
           3: 7,
           7: 8,}

for code in lines:
    input = [c for c in code.split('|')[0].split()]
    output = [c for c in code.split('|')[1].split()]
    for k in output:
        if len(k) in decoder:
            counter[decoder[len(k)]] += 1

print('part 1')
print(sum([q for q in counter.values()]))
'''
0 - 6
1 - 2
2 - 5
3 - 5
4 - 4
5 - 5
6 - 6
7 - 3
8 - 7
9 - 6
'''
def create_builder(input, output):
    decoder = {2: 1,
               4: 4,
               3: 7,
               7: 8,}

    input_digits = [None, None, None, None, None, None, None, None, None, None]
    output_digits = [None, None, None, None]
    total_digits = input_digits + output_digits
    all_digits = input + output

    for i in range(len(all_digits)):
        if len(all_digits[i]) in decoder:
            total_digits[i] = decoder[len(all_digits[i])]

    new_decode = {}
    for j in range(len(total_digits)):
        if total_digits[j] is not None:
            new_decode[total_digits[j]] = all_digits[j]
            # print(all_digits[j])
        else:
            one_idx = total_digits.index(1)
            four_idx = total_digits.index(4)
            if len(all_digits[j]) == 5:
                #possible values 2,3,5
                if all_digits[one_idx][0] in all_digits[j] and all_digits[one_idx][1] in all_digits[j]:
                    total_digits[j] = 3
                else:
                    if len(set(sorted(all_digits[four_idx])) & set(sorted(all_digits[j]))) == 2:
                        total_digits[j] = 2
                    else:
                        total_digits[j] = 5
            elif len(all_digits[j]) == 6:
                # possible values: 0,6,9
                if len(set(sorted(all_digits[four_idx])) & set(sorted(all_digits[j]))) == 4:
                    total_digits[j] = 9
                elif len(set(sorted(all_digits[four_idx])) & set(sorted(all_digits[j]))) == 3:
                    if len(set(sorted(all_digits[one_idx])) & set(sorted(all_digits[j]))) == 2:
                        total_digits[j] = 0
                    else:
                        total_digits[j] = 6


    return total_digits

output_sum = 0
for code in lines:
    input = [c for c in code.split('|')[0].split()]
    output = [c for c in code.split('|')[1].split()]
    decoded = create_builder(input, output)

    output_sum += int(''.join([str(x) for x in decoded[-4:]]))

print('part 2:')
print(output_sum)



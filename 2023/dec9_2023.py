with open("dec9_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

sequences = []
for l in lines:
    sequences.append([int(n) for n in l.split()])

def get_diffs(seq):
    return list(reversed([seq[i] - seq[i-1] for i in range(len(seq)-1,0,-1)]))

big_step_list = []
for seq in sequences:
    new_seq = seq
    steps = 0
    step_lists = []
    step_lists.append(seq)
    while len(set(new_seq)) != 1:
        new_seq = get_diffs(new_seq)
        steps += 1
        step_lists.append(new_seq)

    #one more step
    new_seq = get_diffs(new_seq)
    steps +=1
    step_lists.append(new_seq)

    big_step_list.append(step_lists)

total_one = 0
for d in big_step_list:
    for j in range(len(d)-1,-1,-1):
        if j == len(d)-1:
            d[j].append(0)
        else:
            new_pred = d[j+1][-1] + d[j][-1]
            d[j].append(new_pred)
            if j == 0:
                total_one += new_pred

print("answer part one:", total_one)

total_two = 0
for d in big_step_list:
    for j in range(len(d)-1,-1,-1):
        if j == len(d)-1:
            d[j].append(0)
        else:
            new_pred = d[j][0] - d[j+1][0]
            d[j] = [new_pred] + d[j]
            if j == 0:
                total_two += new_pred

print("answer part two:", total_two)


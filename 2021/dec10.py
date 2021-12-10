with open('dec10.txt') as f:
    lines = [t.strip() for t in f.readlines()]

pairs = {'[': ']',
         '(': ')',
         '{': '}',
         '<': '>'
        }

inv_pairs = {k: v for v, k in pairs.items()}

openers  = [k for k in pairs.keys()]
closers = [v for v in pairs.values()]

illegal_chs = []
corrupt_idx = []
for i, line in enumerate(lines):
    most_recent_open = []
    for ch in line:
        if ch in openers:
            #open
            most_recent_open.append(ch)
        else:
            #close
            if most_recent_open[-1] == inv_pairs[ch]:
                most_recent_open.pop(-1)
            else:
                illegal_chs.append(ch)
                corrupt_idx.append(i)

                break

vals = {']': 57,
         ')': 3,
         '}': 1197,
         '>': 25137
         }
sum = 0
for t in illegal_chs:
    sum += vals[t]
print('part 1:')
print(sum)


#part 2
incomplete = []
for i in range(len(lines)):
    if i not in corrupt_idx:
        incomplete.append(lines[i])


scores = []
for line in incomplete:
    most_recent_open = []
    for ch in line:
        if ch in openers:
            most_recent_open.append(ch)
        else:
            most_recent_open.pop(-1)

    pt2_prod = 0
    pt2_vals = {']': 2,
                       ')': 1,
                       '}': 3,
                       '>': 4
                       }

    for ch in reversed(most_recent_open):
        pt2_prod = pt2_prod*5 + pt2_vals[pairs[ch]]

    scores.append(pt2_prod)

scores.sort()
print('part 2:')
print(scores[len(scores)//2])
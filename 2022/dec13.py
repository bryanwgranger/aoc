with open('dec13ex.txt', 'r') as f:
    lines = [t.strip() for t in f.readlines()]

print(lines)

right = []
wrong = []
pair_no = 1
for i in range(0, len(lines), 3):
    first = lines[i]
    second = lines[i+1]

    #wrong order - length of elements
    first = eval(first)
    second = eval(second)

    if len(first) > len(second):
        wrong.append(pair_no)
        pair_no += 1
        continue
    else:
        for one, two in zip(first, second):
            print(f"{one} vs {two}")
            if isinstance(one, int) and isinstance(two, int):
                if one > two:
                    #WRONG
                    wrong.append(pair_no)
                    pair_no += 1
                    break

            elif isinstance(one, int) and isinstance(two, list):
                if 1 > len(two):
                    #WRONG
                    wrong.append(pair_no)
                    pair_no += 1
                    break
                else:
                    one = [one]
                    for el_one, el_two in zip(one, two):
                        if el_one > el_two:
                            # WRONG
                            wrong.append(pair_no)
                            pair_no += 1
                            break

            elif isinstance(one, list) and isinstance(two, int):
                if 1 < len(one):
                    #WRONG
                    wrong.append(pair_no)
                    pair_no += 1
                    break

                for el_one, el_two in zip(one, two):
                    if el_one > el_two:
                        #WRONG
                        wrong.append(pair_no)
                        pair_no += 1
                        break

            elif isinstance(one, list) and isinstance(two, list):
                if len(two) < len(one):
                    #WRONG
                    wrong.append(pair_no)
                    pair_no += 1
                    break

                for el_one, el_two in zip(one, two):
                    if el_one > el_two:
                        #WRONG
                        wrong.append(pair_no)
                        pair_no += 1
                        break

        right.append(pair_no)
        pair_no += 1


            # if type(first[i]) == 'int' and type(second[i]) == 'int':
            #     if first[i] >= second[i]:
            #         wrong.append(pair_no)
            #         pair_no += 1
            #         continue
            #     right.append(pair_no)
            #     pair_no += 1




print(right)
print(wrong)
with open('dec2.txt', "r") as f:
    lines = [t.strip() for t in f.readlines()]

score_dict = {'X': 1,
              'Y': 2,
              'Z': 3}

opp_dict = {'A': 1,
            'B': 2,
            'C': 3}

result_dict = {'win': 6,
               'draw': 3,
               'loss': 0}

my_score = 0
pt2_score = 0
for l in lines:
    opponent, me = l.split()
    if opponent == 'A':
        if me == 'X':
            my_score += result_dict['draw'] + score_dict[me]
        if me == 'Y':
            my_score += result_dict['win'] + score_dict[me]
        if me == 'Z':
            my_score += result_dict['loss'] + score_dict[me]
    elif opponent == 'B':
        if me == 'X':
            my_score += result_dict['loss'] + score_dict[me]
        if me == 'Y':
            my_score += result_dict['draw'] + score_dict[me]
        if me == 'Z':
            my_score += result_dict['win'] + score_dict[me]

    elif opponent == 'C':
        if me == 'X':
            my_score += result_dict['win'] + score_dict[me]
        if me == 'Y':
            my_score += result_dict['loss'] + score_dict[me]
        if me == 'Z':
            my_score += result_dict['draw'] + score_dict[me]

    ## part 2

    if me == 'X': #loss
        if opponent == 'A':
            pt2_score += score_dict['Z'] + result_dict['loss']
        if opponent == 'B':
            pt2_score += score_dict['X'] + result_dict['loss']
        if opponent == 'C':
            pt2_score += score_dict['Y'] + result_dict['loss']
    elif me == 'Y': #draw
        pt2_score += opp_dict[opponent] + result_dict['draw']
    elif me == 'Z': #draw
        if opponent == 'A':
            pt2_score += score_dict['Y'] + result_dict['win']
        if opponent == 'B':
            pt2_score += score_dict['Z'] + result_dict['win']
        if opponent == 'C':
            pt2_score += score_dict['X'] + result_dict['win']



print("answer 1:", my_score)

print("answer 2:", pt2_score)
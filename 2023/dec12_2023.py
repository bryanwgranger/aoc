import re
from itertools import product
with open("dec12_2023.ex", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(len(lines))

def test_seq(new_seq, code):
    code = [int(c) for c in code.split(",")]
    num_hash = len([f for f in new_seq if f == "#"])
    if num_hash != sum(code):
        return False
    # hash_pat = re.compile(rf"\\.#{1,3}\\.")
    hash_pat = re.compile(r"#+")
    #print(new_seq)
    matches = []
    ch = 0
    while ch < len(new_seq):
        match = re.match(pattern=hash_pat, string=new_seq[ch:])
        if match:
            #print(len(match.group()))
            #print(match.start())
            #print(match.end())
            matches.append(len(match.group()))
            for i in range(len(matches)):
                if matches[i] != code[i]:
                    return False
            ch += match.end()
        #print(matches, code)
        ch += 1
        if len(matches) > len(code):
            return False
        if matches == code:
            #print("FOUND")
            return True



part1 = False
if part1:
    total_pos = 0
    for line in lines:
        seq, code = line.split()
        seq = [c for c in seq]
        #print("".join(seq))

        mut_pos = [i for i, q in enumerate(seq) if q == "?"]
        # print(mut_pos)
        # print(len(mut_pos))
        perm = list(product(["#","."], repeat=len(mut_pos)))
        #print(perm)

        line_possibilities = 0
        for p in perm:
            new_seq = seq.copy()
            # print(p)
            # print(new_seq)
            for i, mp in enumerate(mut_pos):
                #print(mp, p[i])
                new_seq[mp] = p[i]
                #print(new_seq)
            tester = "".join(new_seq)
            if test_seq(tester, code):
                #print('yeah boy')
                line_possibilities += 1
                total_pos += 1
        #print("possibilities:", line_possibilities)
    print("total:", total_pos)

#part2
long_seqs = []
for l in lines:
    seq, code = l.split()
    seq5 = [seq] * 5
    long_seq = "?".join(seq5)
    code5 = [code] * 5
    long_code = ",".join(code5)
    long_seqs.append(long_seq + " " + long_code)

print(long_seqs)
#assert False
total_pos = 0
for t, line in enumerate(long_seqs):
    seq, code = line.split()
    seq = [c for c in seq]
    # print("".join(seq))

    mut_pos = [i for i, q in enumerate(seq) if q == "?"]
    # print(mut_pos)
    # print(len(mut_pos))
    perm = product(["#", "."], repeat=len(mut_pos))
    # print(perm)

    line_possibilities = 0
    for p in perm:
        new_seq = seq.copy()
        # print(p)
        # print(new_seq)
        for i, mp in enumerate(mut_pos):
            # print(mp, p[i])
            new_seq[mp] = p[i]
            # print(new_seq)
        tester = "".join(new_seq)
        if test_seq(tester, code):
            # print('yeah boy')
            line_possibilities += 1
            total_pos += 1
    # print("possibilities:", line_possibilities)
    print(t, "lines")
print("total:", total_pos)
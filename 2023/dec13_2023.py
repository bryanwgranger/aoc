with open("dec13_2023.ex", "r") as infile:
    lines = infile.read().split("\n\n")

print(lines)
print(len(lines))

patterns = []
for l in lines:
    patterns.append([p for p in l.split("\n") if p])

print(patterns)
print(len(patterns))

# patterns = []
# sub_pattern = []
# for i, l in enumerate(lines):
#     if i == len(lines)-1:
#         pass
#
#     if l:
#         sub_pattern.append(l)
#     else:
#         patterns.append(sub_pattern)
#         sub_pattern = []
#         continue
print(patterns)
#columns
column_match_idx = []

def transpose_patterns(patterns):
    transposed = []
    for k, pat in enumerate(patterns):
        print(k)
        new_pat = []
        for j in range(len(pat[0])):
            new_row = []
            for i in range(len(pat)):
                new_row.append(pat[i][j])
            new_pat.append("".join(new_row))
        transposed.append(new_pat)
    return transposed

def find_mirror(patterns):

    match_idx = []
    for pat in patterns:
        col_1 = 1
        col_2 = 2
        print(pat)
        while col_1 != 0 and col_2 != len(pat):
            mirror = False
            print(col_1, col_2)
            print("compare", pat[col_1-1], "vs", pat[col_2-1])
            if pat[col_1-1] == pat[col_2-1]:
                mirror = True
                print('match')
                print(len(pat))
                for j in range(0, min(col_1, len(pat)-col_2)):
                    print(j)
                    step = j + 1
                    print("compare2", pat[col_1 - 1 - step], "vs", pat[col_2 - 1 + step])
                    if pat[col_1-1-step] != pat[col_2-1+step]:

                        mirror = False
                    col_1 += 1
                    col_2 += 1

            else:
                col_1 += 1
                col_2 += 1
            if mirror:
                match_idx.append(col_1)
                continue

    return match_idx

print(patterns[1])
rows = find_mirror(patterns)
cols = find_mirror(transpose_patterns(patterns))
print(rows)
print(cols)
assert False
for q, pat in enumerate(patterns):
    print(len(pat))
    #for p in pat:
    i = 1
    while i != 0 and i != len(pat):
        lower_bound = 0
        upper_bound = len(pat)
        mirror = False
        print("PAT", q, i, "EVAL:", pat[i-1], 'vs', pat[i])
        if pat[i-1] == pat[i]:
            print('match!')
            matches = 1
            print("+++++match range", i, upper_bound-i)
            lim = upper_bound-i
            mirror = True
            if i == 1 or i == len(pat)-1:
                print("BIG match found")
                print("cols", i, i + 1)
                column_match_idx.append(i)
            for j in range(1,min(i+1, upper_bound-i)):

                print("\tEVAL:", pat[i-j-1], 'vs', pat[i + j])
                print("i,j:", i, j )
                print('i-j-1', i-j-1, "i+j", i+j)
                if pat[i-j-1] != pat[i+j]:
                    mirror = False
                    print("\t\tmatches over")
                    #i += 1
                    break
                matches += 1
                print("match", matches)
                #mirror = True
                #print('mirror', q, i, pat[i])
            if j == min(i, upper_bound-i)-1 and mirror:
                print("BIG match found")
                print("cols",i, i+1)
                column_match_idx.append(i)
                break
        i += 1
print("column match indices:", column_match_idx)
print(len(column_match_idx))
print(len(patterns))

#make rows

with open("test.ex", "w") as testfile:
    for pat in patterns:
        testfile.write("\n".join(pat))
        testfile.write("\n\n")
def transpose_patterns(patterns):
    transposed = []
    for k, pat in enumerate(patterns):
        print(k)
        new_pat = []
        for j in range(len(pat[0])):
            new_row = []
            for i in range(len(pat)):
                new_row.append(pat[i][j])
            new_pat.append("".join(new_row))
        transposed.append(new_pat)
    return transposed

row_patterns = transpose_patterns(patterns)

print(patterns)
print(row_patterns)

# for q, pat in enumerate(row_patterns):
#     #print(len(pat))
#     #for p in pat:
#     i = 1
#     while i != 0 and i != len(pat) - 1:
#         lower_bound = 0
#         upper_bound = len(pat)-1
#         mirror = False
#         print("PAT", q, i, "EVAL:", pat[i], 'vs', pat[i+1])
#         if pat[i] == pat[i+1]:
#             print('match!')
#             matches = 1
#             print("+++++match range", i, upper_bound-i)
#             lim = upper_bound-i
#             mirror = True
#             for j in range(1,min(i+1, upper_bound-i)):
#
#                 print("\tEVAL:", pat[i-j], 'vs', pat[i + 1 + j])
#                 if pat[i-j] != pat[i+1+j]:
#                     mirror = False
#                     print("\t\tmatches over")
#                     break
#                 matches += 1
#                 print("match", matches)
#                 #mirror = True
#                 #print('mirror', q, i, pat[i])
#             if j == min(i, upper_bound-i)-1 and mirror:
#                 print("BIG match found")
#                 print("cols",i+1, i+2)
#                 if i == 2:
#                     print("appending 3 here")
#                 row_match_idx.append(i+1)
#                 break
#         i += 1
# print("row match indices:", row_match_idx)
# print(len(row_match_idx))
# #print(len(patterns))




########## TEST
print("-"*60)
row_match_idx = []
for q, pat in enumerate(row_patterns):
    print(len(pat))
    #for p in pat:
    i = 1
    while i != 0 and i != len(pat):
        lower_bound = 0
        upper_bound = len(pat)
        mirror = False
        print("PAT", q, i, "EVAL:", pat[i-1], 'vs', pat[i])
        if pat[i-1] == pat[i]:
            print('match!')
            matches = 1
            print("+++++match range", i, upper_bound-i)
            lim = upper_bound-i
            mirror = True
            if i == 1 or i == len(pat)-1:
                print("BIG match found")
                print("cols", i, i + 1)
                row_match_idx.append(i)
                break
            for j in range(1,min(i+1, upper_bound-i)):

                print("\tEVAL:", pat[i-j-1], 'vs', pat[i + j])
                print("i,j:", i, j )
                print('i-j-1', i-j-1, "i+j", i+j)
                if pat[i-j-1] != pat[i+j]:
                    mirror = False
                    print("\t\tmatches over")
                    #i += 1
                    break
                matches += 1
                print("match", matches)
                #mirror = True
                #print('mirror', q, i, pat[i])
            if j == min(i, upper_bound-i)-1 and mirror:
                print("BIG match found")
                print("cols",i, i+1)
                row_match_idx.append(i)
                break
        i += 1
print("row match indices:", row_match_idx)
print(len(row_match_idx))
print("column match indices:", column_match_idx)
print(len(column_match_idx))
######
total = 0
for r in row_match_idx:
    total += r
for c in column_match_idx:
    total += c * 100
print(total)
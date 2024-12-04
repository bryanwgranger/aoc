lines = [list(a) for a in ["abcd", "efgh", "ijkl"]]

print(lines)

# TRANSPOSE
transposed = []
for i in range(len(lines[0])):
    new_line = []
    for j in range(len(lines)):
        print(i, j, lines[j][i])
        new_line.append(lines[j][i])
    transposed.append(new_line)

print(transposed)
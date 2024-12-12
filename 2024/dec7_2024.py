from itertools import combinations_with_replacement, product, permutations
with open("dec7_2024.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

print(lines)
operators = ["+", "*"]
operators2 = ["+", "*", "||"]
sum_part_one = 0
sum_part_two = 0
for line in lines:
    ans = line.split(":")[0]
    numbers = line.split(": ")[-1].split()
    op_combos = product(operators, repeat=len(numbers)-1)
    #print(list(op_combos))
    test_eqs = []
    for i,o in enumerate(op_combos):
        #p = ""
        ps = int(numbers[0])
        for j,op in enumerate(o):
            #p += f"{numbers[j]}{op}"
            if op == "+":
                ps += int(numbers[j+1])
            if op == "*":
                ps *= int(numbers[j+1])
        #p += f"{numbers[-1]}"
        #print(p, eval(p))
        #print("ps", ps)

        if ps == int(ans):
            #print(p, eval(p))
            #print(ps)
            sum_part_one += ps
            break

            #print(eval(p) == int(ans))

print(sum_part_one)

####PART2
for line in lines:
    ans = line.split(":")[0]
    numbers = line.split(": ")[-1].split()
    op_combos = product(operators2, repeat=len(numbers)-1)
    #print(list(op_combos))
    test_eqs = []
    for i,o in enumerate(op_combos):
        ps = int(numbers[0])
        for j,op in enumerate(o):
            #p += f"{numbers[j]}{op}"
            if op == "+":
                ps += int(numbers[j+1])
            if op == "*":
                ps *= int(numbers[j+1])
            if op == "||":
                ps = int(str(ps)+numbers[j+1])
        #p += f"{numbers[-1]}"
        #print(p, eval(p))
        #print("ps", ps)

        if ps == int(ans):
            #print(p, eval(p))
            #print(ps)
            sum_part_two += ps
            break
print(sum_part_two)

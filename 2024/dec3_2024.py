with open("dec3_2024.input", "r") as infile:
    lines = infile.read()
import re

patt = r"mul\((\d*),(\d*)\)"

results = re.findall(patt, lines)
sum = 0
for x, y in results:
    sum += int(x) * int(y)

print("part 1:", sum)

do_lines = lines.split("do()")
valid_muls = []
for i, d in enumerate(do_lines):
    dont_split = d.split("don't()")
    valid_muls.extend(re.findall(patt, dont_split[0]))

sum_p2 = 0
for x, y in valid_muls:
    sum_p2 += int(x) * int(y)
print("part 2:", sum_p2)
import re

with open("dec1_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

#part 1
part_1 = 0
for line in lines:
    line_digits = []
    for ch in line:
        if ch in '1234567890':
            line_digits.append(ch)
    line_number = str(line_digits[0]) + str(line_digits[-1])
    part_1 += int(line_number)

print("answer part one:", part_1)

#part2
part_2 = 0
num_map = {"one": 1,
           "two": 2,
           "three": 3,
           "four": 4,
           "five": 5,
           "six": 6,
           "seven": 7,
           "eight": 8,
           "nine": 9
           }

nums = re.compile(r"[1-9]|one|two|three|four|five|six|seven|eight|nine")

for line in lines:
    line2_digits = []

    for i in range(len(line)):
        if nums.match(line[i:]):
            line2_digits.append(nums.match(line[i:]).group(0))

    first_num = str(line2_digits[0]) if line2_digits[0].isdigit() else str(num_map[line2_digits[0]])
    last_num = str(line2_digits[-1]) if line2_digits[-1].isdigit() else str(num_map[line2_digits[-1]])

    part_2 += int(first_num + last_num)

print("answer part two:", part_2)
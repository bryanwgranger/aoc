with open("dec2_2023.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

total = 0
power_total = 0
for line in lines:
    game_number = line.split(":")[0].split()[-1]
    dice = line.split(":")[-1].replace(";",",")
    state = True

    red_colors = []
    blue_colors = []
    green_colors = []

    for d in dice.split(","):
        num = d.split()[0]
        color = d.split()[-1]
        if color == 'red':
            if int(num) > 12:
                state = False
            red_colors.append(int(num))
        elif color == 'green':
            if int(num) > 13:
                state = False
            green_colors.append(int(num))
        elif color == 'blue':
            if int(num) > 14:
                state = False
            blue_colors.append(int(num))

    red_max = max(red_colors) #if len(red_colors) > 0 else 1
    green_max = max(green_colors) #if len(green_colors) > 0 else 1
    blue_max = max(blue_colors) #if len(blue_colors) > 0 else 1

    if state:
        total += int(game_number)
    power_total += red_max * blue_max * green_max


print("answer part one:", total)
print("answer part two:", power_total)





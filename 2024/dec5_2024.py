from collections import defaultdict

with open("dec5_2024.input", "r") as infile:
    lines = [t.strip() for t in infile.readlines()]

orders = [l for l in lines if "|" in l]
updates = [u for u in lines if "," in u]

order_dict = defaultdict(list)
rev_order_dict = defaultdict(list)
for entry in orders:
    first, second = entry.split("|")
    order_dict[first].append(second)
    rev_order_dict[second].append(first)

def test_correct(update):
    if not isinstance(update, list):
        update = update.split(",")
    current_update = update
    current_correct = True
    new_list = [a for a in current_update]
    for i, current_page in enumerate(current_update):
        for j in range(i, len(new_list)):
            if current_page in order_dict[new_list[j]]:
                current_correct = False

    return current_correct

incorrect_updates = []
sum_part_one = 0

for update in updates:
    if test_correct(update):
        sum_part_one += int(update.split(",")[len(update.split(",")) // 2])
    else:
        incorrect_updates.append(update)

print("part1:", sum_part_one)

sum_part_two = 0
for current_update in incorrect_updates:
    new_list = [a for a in current_update.split(",")]
    while not test_correct(new_list):
        for i, current_page in enumerate(new_list):
            for j in range(i, len(new_list)):
                if current_page in order_dict[new_list[j]]:
                    #i = index of wrong page
                    #j = index the wrong page must be after
                    tmp = new_list[i]
                    new_list[i] = new_list[j]
                    new_list[j] = tmp
    sum_part_two += int(new_list[len(new_list)//2])

print("part 2:", sum_part_two)
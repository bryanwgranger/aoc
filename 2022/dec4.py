with open('dec4.txt', 'r') as f:
    lines = [t.strip() for t in f.readlines()]

answer_one = 0
answer_two = 0
for l in lines:
    first = l.split(",")[0]
    second = l.split(",")[-1]

    if int(first.split("-")[0]) <= int(second.split("-")[0]) and int(first.split("-")[-1]) >= int(second.split("-")[-1]):
        answer_one += 1
    elif int(second.split("-")[0]) <= int(first.split("-")[0]) and int(second.split("-")[-1]) >= int(first.split("-")[-1]):
        answer_one += 1

    #part 2

    if int(first.split("-")[0]) <= int(second.split("-")[0]) and \
            int(first.split("-")[-1]) >= int(second.split("-")[0]):
        answer_two += 1
    elif int(first.split("-")[0]) <= int(second.split("-")[-1]) and \
            int(first.split("-")[-1]) >= int(second.split("-")[0]):
        answer_two += 1

print("answer 1:", answer_one)
print("answer 2:", answer_two)


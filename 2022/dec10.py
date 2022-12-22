with open('dec10.txt', 'r') as f:
    lines = [t.strip() for t in f.readlines()]

c = 1
i = 0
X = 1

check_points = [20,60,100,140,180,220]
c_dict = {c:0 for c in check_points}

screen = [[0 for _ in range(40)] for k in range(6)]
def spos(X,c):
    if (c-1) % 40 == 0:
        return [X, X+1, X+2]
    elif (c-1) % 40 == 39:
        return [X-2, X-1, X]
    else:
        return [X-1,X,X+1]

def get_line(c):
    return (c // 40)

def get_col(c):
    return (c-1) % 40

def draw_pix(c, X, screen):
    if get_col(c) in spos(X,c):
        screen[get_line(c)][get_col(c)] = "#"
    else:
        screen[get_line(c)][get_col(c)] = "."

while c < 240:
    if lines[i].startswith("noop"):

        #part2
        draw_pix(c, X, screen)
        c += 1
    else:
        cmd, val = lines[i].split()
        #addx begins - cycle 1
        #check c
        if c in c_dict.keys():
            c_dict[c] = X * c
        draw_pix(c, X, screen)
        c += 1
        #last cycle for addx, X changes after this

        #check c
        if c in c_dict.keys():
            c_dict[c] = X * c
        draw_pix(c, X, screen)
        c += 1
        X += int(val)
        if c in c_dict.keys():
            c_dict[c] = X * c
    i += 1

print('answer1:',sum(c_dict.values()))

#part 2
for l in screen:
    l = [str(h) for h in l]
    print("".join(l))
with open('dec9ex.txt', 'r') as f:
    lines = [t.strip() for t in f.readlines()]

import plotly.graph_objects as go



def check_tail_pos(head_point, tail_point):
    #horizontal
    if head_point[1] == tail_point[1] and abs(head_point[0] - tail_point[0]) > 1:
        return 'horizontal'
    #vertical
    elif head_point[0] == tail_point[0] and abs(head_point[1] - tail_point[1]) > 1:
        return 'vertical'
    #diagonal
    elif head_point != tail_point and (abs(head_point[0] - tail_point[0]) >= 2 or abs(head_point[1] - tail_point[1]) >= 2):
        return 'diagonal'
    elif head_point == tail_point:
        return 'same'
    else:
        return 'no change'

def check_nine_pos(head_point, nine_point):
    #horizontal
    if head_point[1] == tail_point[1] and abs(head_point[0] - tail_point[0]) > 9:
        return 'horizontal'
    #vertical
    elif head_point[0] == tail_point[0] and abs(head_point[1] - tail_point[1]) > 9:
        return 'vertical'
    #diagonal
    elif head_point != tail_point and (abs(head_point[0] - tail_point[0]) >= 2 or abs(head_point[1] - tail_point[1]) >= 2):
        return 'diagonal'
    elif head_point == tail_point:
        return 'same'
    else:
        return 'no change'

#x,y
head_point = [0,0]
tail_point = [0,0]
tail_history = []

for c in lines:
    direction, dist = c.split()
    dist = int(dist)
    if direction == 'U':
        for m in range(dist):
            head_point[1] += 1
            #print(check_tail_pos(head_point, tail_point))
            if check_tail_pos(head_point, tail_point) == 'vertical':
                tail_point[1] += 1
            elif check_tail_pos(head_point, tail_point) == 'diagonal':
                tail_point[0] = head_point[0]
                tail_point[1] += 1
            tail_history.append((tail_point[0], tail_point[1]))
    elif direction == 'D':
        for m in range(dist):
            head_point[1] -= 1
            #print(check_tail_pos(head_point, tail_point))
            if check_tail_pos(head_point, tail_point) == 'vertical':
                tail_point[1] -= 1
            elif check_tail_pos(head_point, tail_point) == 'diagonal':
                tail_point[0] = head_point[0]
                tail_point[1] -= 1
            tail_history.append((tail_point[0], tail_point[1]))
    elif direction == 'R':
        for m in range(dist):
            head_point[0] += 1
            #print(check_tail_pos(head_point, tail_point))
            if check_tail_pos(head_point, tail_point) == 'horizontal':
                tail_point[0] += 1
            elif check_tail_pos(head_point, tail_point) == 'diagonal':
                tail_point[1] = head_point[1]
                tail_point[0] += 1
            tail_history.append((tail_point[0], tail_point[1]))
    elif direction == 'L':
        for m in range(dist):
            head_point[0] -= 1
            #print(check_tail_pos(head_point, tail_point))
            if check_tail_pos(head_point, tail_point) == 'horizontal':
                tail_point[0] -= 1
            elif check_tail_pos(head_point, tail_point) == 'diagonal':
                tail_point[1] = head_point[1]
                tail_point[0] -= 1
            tail_history.append((tail_point[0], tail_point[1]))

print("answer 1:", len(set(tail_history)))

#bonus graph of the tail point's movement
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[p[0] for p in tail_history],
    y=[p[1] for p in tail_history]
))
#fig.show()


##part 2
#x,y

ten_points = [[0,0] for _ in range(10)]
print(ten_points)
nine_history = []
for c in lines:
    direction, dist = c.split()
    dist = int(dist)
    print(direction, dist)
    if direction == 'U':
        for m in range(dist):
            ten_points[0][1] += 1
            for i in range(1,len(ten_points)):

                print(i, check_tail_pos(ten_points[i - 1], ten_points[i]))

                if check_tail_pos(ten_points[i-1], ten_points[i]) == 'vertical':
                    ten_points[i][1] += 1
                elif check_tail_pos(ten_points[i-1], ten_points[i]) == 'diagonal':
                    ten_points[i][0] = ten_points[i-1][0]
                    ten_points[i][1] += 1
            print((ten_points[-1][0], ten_points[-1][1]))
            nine_history.append((ten_points[-1][0], ten_points[-1][1]))

    elif direction == 'D':
        for m in range(dist):
            ten_points[0][1] -= 1
            for i in range(1,len(ten_points)):

                print(i, check_tail_pos(ten_points[i - 1], ten_points[i]))

                if check_tail_pos(ten_points[i-1], ten_points[i]) == 'vertical':
                    ten_points[i][1] -= 1
                elif check_tail_pos(ten_points[i-1], ten_points[i]) == 'diagonal':
                    ten_points[i][0] = ten_points[i-1][0]
                    ten_points[i][1] -= 1
            print((ten_points[-1][0], ten_points[-1][1]))
            nine_history.append((ten_points[-1][0], ten_points[-1][1]))

    elif direction == 'R':
        for m in range(dist):
            ten_points[0][0] += 1
            for i in range(1,len(ten_points)):

                print(i, check_tail_pos(ten_points[i - 1], ten_points[i]))

                if check_tail_pos(ten_points[i-1], ten_points[i]) == 'horizontal':
                    ten_points[i][0] += 1
                elif check_tail_pos(ten_points[i-1], ten_points[i]) == 'diagonal':
                    ten_points[i][1] = ten_points[i-1][1]
                    ten_points[i][0] += 1
            print((ten_points[-1][0], ten_points[-1][1]))
            nine_history.append((ten_points[-1][0], ten_points[-1][1]))

    elif direction == 'L':
        for m in range(dist):
            ten_points[0][0] -= 1
            for i in range(1,len(ten_points)):

                print(i, check_tail_pos(ten_points[i-1], ten_points[i]))
                if check_tail_pos(ten_points[i-1], ten_points[i]) == 'horizontal':
                    ten_points[i][0] -= 1
                elif check_tail_pos(ten_points[i-1], ten_points[i]) == 'diagonal':
                    ten_points[i][1] = ten_points[i-1][1]
                    ten_points[i][0] -= 1
            print((ten_points[-1][0], ten_points[-1][1]))
            nine_history.append((ten_points[-1][0], ten_points[-1][1]))

print(nine_history)
print(set(nine_history))
print("answer 2:", len(set(nine_history)))

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[p[0] for p in set(nine_history)],
    y=[p[1] for p in set(nine_history)],
    mode = 'markers'
))
#fig.show()
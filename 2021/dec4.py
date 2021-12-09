import numpy as np

nums = [17,11,37,7,89,48,99,28,56,55,57,27,83,59,53,72,6,87,
        33,82,13,23,35,40,71,47,78,2,39,4,51,1,67,31,79,69,
        15,73,80,22,92,95,91,43,26,97,36,34,12,96,86,52,66,
        94,61,76,64,77,85,98,42,68,84,63,60,30,65,19,54,58,
        24,20,25,75,93,16,18,44,14,88,45,10,9,3,70,74,81,90,
        46,38,21,49,29,50,0,5,8,32,62,41]

with open('dec4.txt') as f:
        n = list(num.strip() for num in f.readlines())
# print(n)

called_nums = []

all_boards = np.zeros((100,5,5))
# print(all_boards)
for i in range(0, 100):
        # if i > 0 and i%5 == 0:
        one_board = np.array([[int(t) for t in n[i*6].split()],
                              [int(t) for t in n[i*6+1].split()],
                              [int(t) for t in n[i*6+2].split()],
                              [int(t) for t in n[i*6+3].split()],
                              [int(t) for t in n[i*6+4].split()]])
        all_boards[i] = one_board

def check_board(board, called_nums):
        #check rows
        for i in range(5):
                if np.sum(np.isin(called_nums, board[i])) == 5:
                        return True
                if np.sum(np.isin(called_nums, board[:,i])) == 5:
                        return True
        return False


#part 1
c = False
i = 0
j = 0

while not c:

        called_nums.append(nums[i])

        # print(f'checking board {j}')
        for j in range(len(all_boards)):

                winner = all_boards[j]
                c = check_board(all_boards[j], np.array(called_nums))
                if c:
                        break
        i += 1

count = 0
for i in range(5):
        for j in range(5):
                if winner[i][j] not in called_nums:
                        count += winner[i][j]

print('part 1:', count * called_nums[-1])

print('end of part 1')
#part 2

c = False
i = 0
non_winning_boards = list(range(100))
called_nums = []

for i in range(100):

        called_nums.append(nums[i])

        for board in non_winning_boards:

                # c = check_board(all_boards[board], np.array(called_nums))
                if check_board(all_boards[board], np.array(called_nums)):
                        non_winning_boards.remove(board)
        print(non_winning_boards)
        print(len(called_nums))
        if len(non_winning_boards) == 1:
                break
print('non winning boards:')
print(non_winning_boards)

loser = all_boards[99]
print(called_nums)

### board 44 is the last one, although this algorithm selected 99 as the last one. ?????

c = False
i = 0
called_nums = []
while not c:
        called_nums.append(nums[i])
        c = check_board(loser, np.array(called_nums))
        i += 1

print('playing loser board')
print(called_nums)
count = 0
for i in range(5):
        for j in range(5):
                if loser[i][j] not in called_nums:
                        count += loser[i][j]
print(count)
print(count * called_nums[-1])
print(len(called_nums))
print(loser)
print(np.isin(loser, np.array(called_nums)))
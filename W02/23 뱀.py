# 뱀

import sys

N = int(sys.stdin.readline())
board = [[0] * (N + 1) for _ in range(N + 1)]
K = int(sys.stdin.readline())
for _ in range(K):
    apple = list(map(int, sys.stdin.readline().split()))
    board[apple[0]][apple[1]] = 1

# snake
board[1][1] = -1
headindex = [1, 1]
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
currentdirection = 0
bodyS = list()
bodyS.append([headindex[0], headindex[1]])

# instructions
L = int(sys.stdin.readline())
insL = list()
for _ in range(L):
    insL.append(list(sys.stdin.readline().split()))
ins = insL.pop(0)
nextturn = int(ins[0])

count = 0

while True:
    count += 1

    headindex[0] += direction[currentdirection][0]
    headindex[1] += direction[currentdirection][1]
    bodyS.insert(0, [headindex[0], headindex[1]])

    if headindex[0] > N or headindex[1] > N or headindex[0] < 1 or headindex[1] < 1 or board[headindex[0]][
        headindex[1]] == -1:
        break
    elif board[headindex[0]][headindex[1]] == 1:
        board[headindex[0]][headindex[1]] = -1
    else:
        board[headindex[0]][headindex[1]] = -1
        tail = bodyS.pop()
        board[tail[0]][tail[1]] = 0

    if count == nextturn:
        if ins[1] == 'L':
            currentdirection = (currentdirection + 3) % 4
        else:  # 'D'
            currentdirection = (currentdirection + 1) % 4

        if insL:
            ins = insL.pop(0)
            nextturn = int(ins[0])

print(count)

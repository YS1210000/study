import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

playing = deque([[0, 0]]) #시작 위치, 주사위 횟수

up = []
down = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    up.append([x-1, y-1])


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    down.append([u-1, v-1])

up.sort(key=lambda a: a[0])
down.sort(key=lambda b: b[0])

board = [0 for _ in range(100)]

result = []

while playing:
    tmp = playing.popleft()
    now = tmp[0]
    count = tmp[1]

    if now == 99:
        result.append(count)

    #print(tmp, now, count)

    board[now] = 1

    for u in up:
        if now is u[0]:
            now = u[1]

    for d in down:
        if now is d[0]:
            now = d[1]

    for i in range(1, 7):
        if now+i < 100 and board[now+1] == 0:
            playing.append([now+i, count+1])

    #print(playing)

sorted(result)

print(result[0])

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

q = deque([[N, 0]])
arr = [200004 for i in range(999999)]


while q:
    now = q.popleft()
    #print(now)

    if now[0] == K:
        print(now[1])
        break

    next_sec = now[1] + 1
    if now[0] - 1 >= 0 and arr[now[0] - 1] > next_sec:
        q.append([now[0] - 1, next_sec])
        arr[now[0] - 1] = next_sec
    if arr[now[0] + 1] > next_sec:
        q.append([now[0] + 1, next_sec])
        arr[now[0] + 1] = next_sec
    if 200004 > now[0] * 2 >= 0 and arr[now[0] * 2] > next_sec:
        q.append([now[0] * 2, next_sec])
        arr[now[0] * 2] = next_sec

    #print(q)

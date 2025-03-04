import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

tomato = []

for i in range(m):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    tomato.append(tmp)

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]

def BFS(v):
    q = deque(v)

    while q:
        #print(q)
        node = q.popleft()
        #print(node)
        days = node[2]

        for i in range(4):
            next_x = node[0] + x[i]
            next_y = node[1] + y[i]

            if 0 <= next_x < m and 0 <= next_y < n and tomato[next_x][next_y] == 0:
                q.append([next_x, next_y, days + 1])
                tomato[next_x][next_y] = 1

    return days

starts = []

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            starts.append([i, j, 0])

if starts:
    result = BFS(starts)
else:
    print("-1")
    exit(0)

fail_chk = False

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            fail_chk = True

if fail_chk is True:
    print(-1)
else:
    print(result)

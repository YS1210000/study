import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
mage = []

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    mage.append(list(map(int, tmp)))

q = deque([[0, 0, 1]])
mage[0][0] = 0

x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]


while q:
    node = q.popleft()
    #print(node)
    dis = node[2]
    if node[0] == n-1 and node[1] == m-1:
        print(dis)
        break
    dis += 1


    for i in range(4):
        next_x = node[0] + x[i]
        next_y = node[1] + y[i]

        if 0 <= next_x < n and 0 <= next_y < m and mage[next_x][next_y] == 1:
            mage[next_x][next_y] = 0
            q.append([next_x, next_y, dis])

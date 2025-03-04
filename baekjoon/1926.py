import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
pic = []

x = [-1, 0, 0, 1]
y = [0, 1, -1, 0]

for i in range(n):
    pic.append(list(map(int, sys.stdin.readline().rstrip().split())))

def BFS(v):
    q = deque(v)
    pic[v[0][0]][v[0][1]] = 0
    size = 1

    while q:
        node = q.popleft()
        #print(node)

        for i in range(4):
            next_x = node[0] + x[i]
            next_y = node[1] + y[i]

            if 0 <= next_x < n and 0 <= next_y < m and pic[next_x][next_y] == 1:
                pic[next_x][next_y] = 0
                q.append([next_x, next_y])
                size += 1

    return size

count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if pic[i][j] == 1:
            count += 1
            max_size = max(max_size, BFS([[i, j]]))

print(count)
print(max_size)

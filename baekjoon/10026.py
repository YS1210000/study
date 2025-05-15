import sys
from sys import setrecursionlimit

setrecursionlimit(10**5)

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    arr.append(tmp)

visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(v):
    visited[v[0]][v[1]] = True

    for i in range(4):
        next_x = v[0] + dx[i]
        next_y = v[1] + dy[i]

        if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] is False and arr[v[0]][v[1]] == arr[next_x][next_y]:
            DFS((next_x, next_y))

result = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            DFS((i, j))
            result += 1

for i in range(n):
    for j in range(n):
        if arr[i][j] == "G":
            arr[i][j] = "R"

result2 = 0
visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] is False:
            DFS((i, j))
            result2 += 1

print(result, result2)

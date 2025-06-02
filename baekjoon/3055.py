import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
arr = []
for _ in range(r):
    arr.append(list(sys.stdin.readline().rstrip()))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            a = i
            b = j

def bfs(a, b):
    q = deque([(a, b)])
    visited = [[False for _ in range(c)] for _ in range(r)]
    count = 0

    while q:
        repeat = len(q)

        count += 1

        for j in range(repeat):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and arr[x][y] == "S" and visited[nx][ny] is False:

                    if arr[nx][ny] == "D":
                        return count
                    elif arr[nx][ny] == ".":
                        visited[nx][ny] = True
                        arr[nx][ny] = "S"
                        q.append((nx, ny))

        water = []
        for i in range(r):
            for j in range(c):
                if arr[i][j] == '*':

                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != "D" and arr[nx][ny] != "X":
                            water.append((nx, ny))

        for x, y in water:
            arr[x][y] = "*"

        '''for i in arr:
            print(*i)
        print()'''
    return "KAKTUS"

print(bfs(a, b))

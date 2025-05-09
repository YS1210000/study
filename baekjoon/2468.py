import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(a, b, start):
    q = []
    q.append([a, b])

    while q:
        x, y = q.pop()
        visited[x][y] = True
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] is False and arr[next_x][next_y] >= start:
                q.append([next_x, next_y])

start = 1
answer = []
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]

    result = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] is False and arr[x][y] >= start:
                DFS(x, y, start)
                result += 1

    if result == 0:
        break
    else:
        answer.append(result)
    start += 1

print(max(answer))

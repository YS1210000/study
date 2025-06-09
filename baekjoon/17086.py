import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

def BFS(q, rec):
    next_q = []
    while q:
        x, y = q.pop()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] is False and arr[nx][ny] == 0:
                visited[nx][ny] = True
                arr[nx][ny] = 1
                next_q.append((nx, ny))

    if next_q:
        BFS(next_q, rec+1)
    else:
        print(rec)


q = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

BFS(q, 0)

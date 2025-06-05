import sys

m, n, k = map(int, sys.stdin.readline().split())
arr = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    ax, ay, bx, by = map(int, sys.stdin.readline().split())
    for i in range(ax, bx):
        for j in range(ay, by):
            arr[j][i] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = []
visited = [[False for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            size = 0
            q = [(i, j)]
            while q:
                size += 1
                x, y = q.pop()
                for c in range(4):
                    nx = x + dx[c]
                    ny = y + dy[c]

                    if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0 and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = True
            result.append(size)
            count += 1
print(count)
print(*sorted(result))

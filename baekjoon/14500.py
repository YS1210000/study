import sys

n, m = map(int, sys.stdin.readline().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False for _ in range(m)] for _ in range(n)]


result = 0

def dfs(v, q, count):
    global result

    if count < 4:
        for i in range(4):
            next_x = v[0] + dx[i]
            next_y = v[1] + dy[i]
            if 0 <= next_x < n and 0 <= next_y < m and visited[next_x][next_y] is False:
                visited[next_x][next_y] = True
                dfs((next_x, next_y), q + arr[next_x][next_y], count + 1)
                visited[next_x][next_y] = False
    else:
        result = max(result, q)

def other_search(v):
    global result

    q = []
    for i in range(4):
        next_x = v[0] + dx[i]
        next_y = v[1] + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            visited[next_x][next_y] = True
            q.append(arr[next_x][next_y])
            visited[next_x][next_y] = False

    if len(q) == 4:
        q.sort(reverse=True)
        q.pop()
        q.append(arr[v[0]][v[1]])
        result = max(result, sum(q))
    elif len(q) == 3:
        q.append(arr[v[0]][v[1]])
        result = max(result, sum(q))


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs((i, j), arr[i][j], 1)
        other_search((i, j))
        visited[i][j] = False

print(result)

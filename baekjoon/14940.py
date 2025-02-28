import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = []
visited = [[0 for _ in range(M)] for _ in range(N)]
def BFS(v):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([v])

    while q:
        dir = q.popleft()

        if arr[dir[0]][dir[1]] != 0:
            arr[dir[0]][dir[1]] += dir[2]
            k = arr[dir[0]][dir[1]]
            for i in range(4):
                next_x = dir[0] + dx[i]
                next_y = dir[1] + dy[i]

                if 0 <= next_x < N and 0 <= next_y < M and visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = 1
                    q.append([next_x, next_y, k])



for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(tmp)
    for j in range(M):
        if tmp[j] == 2:
            start = [i, j]

BFS([start[0], start[1], -2])

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0 and visited[i][j] == 0:
            print("-1", end=' ')
        else:
            print(arr[i][j], end=' ')
    print()

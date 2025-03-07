import sys
from collections import deque
T = int(sys.stdin.readline())

dir_x = [-1, 1, 0, 0]
dir_y = [0, 0, -1, 1]

def BFS(a, b):
    q = deque([[a, b]])

    while q:
        node = q.popleft()

        for i in range(4):
            next_x = node[0] + dir_x[i]
            next_y = node[1] + dir_y[i]

            if M > next_x >= 0 and N > next_y >= 0 and arr[next_y][next_x] == 1:
                q.append([next_x, next_y])
                #print(next_x, next_y)
                arr[next_y][next_x] = 0

    return arr


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    arr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1

    result = 0
    for j in range(M):
        for k in range(N):
            if arr[k][j] == 1:
                result += 1
                BFS(j, k)
                #print(arr)

    print(result)

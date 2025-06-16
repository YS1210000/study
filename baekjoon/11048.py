import sys

n, m = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

table = [[0 for _ in range(m)] for _ in range(n)]
table[0][0] = arr[0][0]

dx = [1, 0, 1]
dy = [0, 1, 1]

for i in range(n):
    for j in range(m):
        for k in range(3):
            ny = i + dy[k]
            nx = j + dx[k]

            if nx < m and ny < n:
                table[ny][nx] = max(arr[ny][nx] + table[i][j], table[ny][nx])

        '''for a in table:
            print(*a)
        print()'''

print(table[n-1][m-1])

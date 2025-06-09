import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

table = [[0 for _ in range(n)] for _ in range(n)]
table[0][0] = 1

dx = [1, 0]
dy = [0, 1]

for y in range(n):
    for x in range(n):
        if table[y][x] == 0:
            continue

        if arr[y][x] == 0:
            continue

        for i in range(2):
            nx = x + dx[i] * arr[y][x]
            ny = y + dy[i] * arr[y][x]

            if 0 <= nx < n and 0 <= ny < n:
                table[ny][nx] += table[y][x]

        '''
        for i in table:
            print(*i)
        print()
        '''

print(table[-1][-1])

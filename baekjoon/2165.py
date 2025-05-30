import sys

arr = []
for _ in range(19):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, 1, 0, 1]
dy = [0, 1, 1, -1]

blacklist = []

def search(y, x, color):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 19 and 0 <= ny < 19 and arr[ny][nx] == color:
            if (nx, ny, i) not in blacklist:
                DFS(ny, nx, i, color)

def DFS(y, x, i, color):
    j = 1
    while True:
        nx = x + dx[i] * j
        ny = y + dy[i] * j
        if 0 <= nx < 19 and 0 <= ny < 19 and arr[ny][nx] == color:
            #print(ny, nx, i)
            j += 1
        else:
            break

    if j == 4:
        print(color)
        print(y - dy[i] + 1, x - dx[i] + 1)
        exit(0)
    elif j > 4:
        for k in range(-1, j):
            nx = x + dx[i] * k
            ny = y + dy[i] * k

            blacklist.append((nx, ny, i))


    return


for i in range(19):
    for j in range(19):
        if arr[j][i] != 0:
            search(j, i, arr[j][i])

print(0)

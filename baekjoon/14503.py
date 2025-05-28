import sys

n, m = map(int, sys.stdin.readline().split())
x, y, d = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, d, count): #-1은 청소된 빈칸, 0은 청소되지않은 빈칸, 1은 벽
    if arr[x][y] == 0:
        arr[x][y] = -1
        count += 1

    isclean = True
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < m and arr[next_x][next_y] == 0:
            isclean = False
            break

    if isclean:
        canmove = d - 2
        if canmove < 0:
            canmove += 4

        next_x = x + dx[canmove]
        next_y = y + dy[canmove]

        if 0 <= next_x < n and 0 <= next_y < m and arr[next_x][next_y] != 1:
            move(next_x, next_y, d, count)
        else:
            print(count)
            return
    else:
        for _ in range(4):
            d -= 1
            if d < 0:
                d += 4

            next_x = x + dx[d]
            next_y = y + dy[d]

            if 0 <= next_x < n and 0 <= next_y < m and arr[next_x][next_y] == 0:
                move(next_x, next_y, d, count)
                break

move(x, y, d, 0)

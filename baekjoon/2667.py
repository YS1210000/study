import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    tmp2 = []
    for j in range(0, n):
        tmp2.append(int(tmp[j]))
    arr.append(tmp2)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    global count
    arr[x][y] = 0
    count += 1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n and arr[next_x][next_y] == 1:
            DFS(next_x, next_y)

result = []
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            count = 0
            DFS(x, y)
            result.append(count)

print(len(result))
result.sort()
for i in result:
    print(i)

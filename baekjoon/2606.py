import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False for _ in range(n+1)]

result = 0
def DFS(v):
    visited[v] = True
    global result

    for i in arr[v]:
        if not visited[i]:
            result += 1
            DFS(i)

DFS(1)

print(result)

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

def DFS(v):
    visited[v] = 1
    for i in arr[v]:
        if not visited[i]:
            DFS(i)

result = 0
for i in range(1, N+1):
    if not visited[i]:
        DFS(i)
        result += 1

print(result)

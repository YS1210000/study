import sys

T = int(sys.stdin.readline())

def DFS(v):
    visited[v] = True
    if visited[arr[v]] is False:
        DFS(arr[v])

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [0]+list(map(int, sys.stdin.readline().split()))
    visited = [False for _ in range(N+1)]
    result = 0

    for i in range(1, N+1):
        if visited[i] is False:
            DFS(i)
            result += 1

    print(result)

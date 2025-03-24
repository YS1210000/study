import sys

N = int(sys.stdin.readline())
arr = [0]
for i in range(N):
    arr.append(int(sys.stdin.readline()))

visited = [False for i in range(N+1)]
result = []

def DFS(v, target):
    if visited[arr[v]] is False:
        visited[arr[v]] = True
        DFS(arr[v], target)
        visited[arr[v]] = False
    if arr[v] == target:
        result.append(target)

for i in range(1, N+1):
    visited[i] = True
    DFS(i, i)
    visited[i] = False

print(len(result))
for i in result:
    print(i)

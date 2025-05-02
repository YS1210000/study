import sys

n = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr = [[]for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

not_cousin = True

def DFS(v, target_v, iter):
    global not_cousin
    visited[v] = True

    if v == target_v:
        print(iter)
        not_cousin = False


    for w in arr[v]:
        if not visited[w]:
            DFS(w, target_v,iter + 1)

DFS(target[0], target[1], 0)

if not_cousin:
    print(-1)

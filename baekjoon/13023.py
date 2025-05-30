import sys
from itertools import count

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    arr[a].append(b)
    arr[b].append(a)

def search(i, count):
    visited[i] = True
    if count == 5:
        print(1)
        exit(0)

    for j in arr[i]:
        if visited[j] is False:
            visited[j] = True
            search(j, count + 1)
            visited[j] = False

visited = [False for _ in range(n)]
for i in range(n):
    search(i, 1)
    visited[i] = False

print(0)

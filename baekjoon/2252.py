import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
q = deque()
result = []

for _ in range(M):
    e1, e2 = map(int, sys.stdin.readline().split())
    graph[e1].append(e2)
    indegree[e2] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    tmp = q.popleft()
    result.append(tmp)
    for i in graph[tmp]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(" ".join(map(str, result)))

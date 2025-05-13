import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().split())

arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = [[0 for _ in range(m)] for _ in range(n)]

cycle = min(n, m) // 2

queue = deque()

for iter in range(cycle):
    for j in range(iter, m - iter):
        queue.append(arr[iter][j])
    for j in range(iter + 1, n - iter - 1):
        queue.append(arr[j][m - iter - 1])
    for j in range(m - iter- 1, iter - 1, -1):
        queue.append(arr[n - iter - 1][j])
    for j in range(n - iter- 2, iter, -1):
        queue.append(arr[j][iter])

    for _ in range(r):
        queue.append(queue.popleft())

    for j in range(iter, m - iter):
        answer[iter][j] = queue.popleft()
    for j in range(iter + 1, n - iter - 1):
        answer[j][m - iter - 1] = queue.popleft()
    for j in range(m - iter- 1, iter - 1, -1):
        answer[n - iter - 1][j] = queue.popleft()
    for j in range(n - iter- 2, iter, -1):
        answer[j][iter] = queue.popleft()

for line in answer:
    print(" ".join(map(str, line)))

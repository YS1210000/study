import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = deque(list(map(int, sys.stdin.readline().split()))) #내구도

robots = deque(0 for _ in range(N))
count = 0

while A.count(0) < K:
    count += 1
    robots.rotate(1)
    A.rotate(1)

    robots[-1] = 0

    for i in range(N - 2, -1, -1):
        if A[i+1] > 0 and robots[i] == 1 and robots[i+1] == 0:
            robots[i+1] = 1
            A[i+1] -= 1
            robots[i] = 0

    robots[-1] = 0

    if A[0] > 0:
        robots[0] = 1
        A[0] -= 1

    #print(robots, A)

print(count)

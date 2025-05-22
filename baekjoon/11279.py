import sys
import heapq

n = int(sys.stdin.readline())

q = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -tmp)

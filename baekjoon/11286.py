import sys
import heapq

n = int(sys.stdin.readline())

q = []

for _ in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0:
        if q:
            a = heapq.heappop(q)
            print(a[0] * a[1])
        else:
            print(0)
    else:
        if tmp >= 0:
            minus = 1
        else:
            minus = -1
        heapq.heappush(q, [abs(tmp), minus])

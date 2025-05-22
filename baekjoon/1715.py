import sys
import heapq

n = int(sys.stdin.readline())

q = []
for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline()))

ans = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    heapq.heappush(q, a+b)
    ans += a + b

print(ans)

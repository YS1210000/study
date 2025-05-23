import sys
import heapq

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key = lambda x: (x[0], -x[1]))
#print(arr)

q = []
for deadline, ramen in arr:
    if deadline > len(q):
        heapq.heappush(q, ramen)
    else:
        tmp = heapq.heappop(q)
        if tmp > ramen:
            heapq.heappush(q, tmp)
        else:
            heapq.heappush(q, ramen)
    #print(q, deadline)

print(sum(q))

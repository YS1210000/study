import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = []

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in tmp:
        if len(arr) < N:
            heapq.heappush(arr, j)
        elif arr[0] < j:
            heapq.heappop(arr)
            heapq.heappush(arr, j)

print(heapq.heappop(arr))

'''메모리 초과
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in tmp:
        heapq.heappush(arr, -j)

for _ in range(N-1):
    heapq.heappop(arr)

print(-heapq.heappop(arr))
'''

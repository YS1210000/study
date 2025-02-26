import heapq, sys

arr = []

n = int(sys.stdin.readline())

for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if len(arr) != 0:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, tmp)

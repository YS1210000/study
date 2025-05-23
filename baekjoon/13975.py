import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    heapq.heapify(arr)

    result = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)

        tmp = a + b
        result += a + b
        heapq.heappush(arr, tmp)

    print(result)

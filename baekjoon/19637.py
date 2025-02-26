import sys

N, M = map(int, sys.stdin.readline().split())

limit = []

for _ in range(N):
    name, num = map(str, sys.stdin.readline().split())
    limit.append([int(num), name])

for label in range(M):
    power = int(sys.stdin.readline().rstrip())

    start = 0
    end = N-1
    up_idx = N

    while start <= end:
        mid = (start + end) // 2

        if power <= limit[mid][0]:
            end = mid - 1
            up_idx = min(up_idx, mid)
        else:
            start = mid + 1

        #print(start, mid, end)

    print(limit[up_idx][1])

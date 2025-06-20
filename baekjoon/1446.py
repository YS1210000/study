import sys

n, d = map(int, sys.stdin.readline().split())

road = [i for i in range(d+1)]
arr = []

for _ in range(n):
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    if end > d:
        continue

    arr.append((start, end, cost))

arr.sort()

for start, end, cost in arr:
    if road[start] + cost < road[end]:
        #print(f"{start} to {end}, before cost: {road[start]}, end cost: {road[start] + cost}")
        road[end] = road[start] + cost

        nc = road[end]
        for i in range(end, d+1):
            if road[i] < nc:
                nc = road[i]

            road[i] = nc
            nc += 1

print(road[d])

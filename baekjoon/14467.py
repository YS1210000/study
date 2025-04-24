import sys

N = int(sys.stdin.readline())
arr = [-1 for _ in range(11)]
result = 0

for _ in range(N):
    cow, road = map(int, sys.stdin.readline().split())
    if arr[cow] == -1:
        arr[cow] = road
    else:
        if arr[cow] != road:
            arr[cow] = road
            result += 1

print(result)

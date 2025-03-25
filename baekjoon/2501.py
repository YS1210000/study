import sys

N, K = map(int, sys.stdin.readline().split())
arr = []

for i in range(1, int(N*0.5+1)):
    if N % i == 0:
        arr.append(i)
        if len(arr) == K:
            print(arr[K-1])
            exit(0)

arr.append(N)
if len(arr) == K:
    print(arr[K - 1])
    exit(0)

print(0)

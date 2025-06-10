import sys

n = int(sys.stdin.readline())
arr = [0 for _ in range(n+1)]
for i in range(1, n+1):
    t, p = map(int, sys.stdin.readline().split())

    arr[i] = max(arr[i], arr[i-1])
    if i + t <= n+1:
        arr[i+t-1] = max(arr[i+t-1], arr[i-1] + p)

print(arr[-1])

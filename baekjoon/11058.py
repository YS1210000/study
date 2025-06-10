import sys

n = int(sys.stdin.readline())
arr = [i for i in range(1, n+1)]

for i in range(6, n):
    arr[i] = max(arr[i-3] * 2, arr[i-4] * 3, arr[i-5] * 4)

print(arr[-1])

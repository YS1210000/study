import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

min_val = sys.maxsize
max_val = -sys.maxsize

for i in range(0, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]

print(min_val, max_val)

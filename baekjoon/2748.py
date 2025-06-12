import sys

arr = [0, 1] + [0 for _ in range(89)]

for i in range(2, 91):
    arr[i] = arr[i-1] + arr[i-2]

n = int(sys.stdin.readline())
print(arr[n])

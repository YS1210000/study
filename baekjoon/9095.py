import sys

arr = [0, 1, 2, 4] + [0 for _ in range(7)]
for i in range(4, 11):
    arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(arr[n])

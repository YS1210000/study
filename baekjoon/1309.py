import sys

n = int(sys.stdin.readline())
arr = [0 for _ in range(max(3, n + 1))]
arr[1] = 3
arr[2] = 7

for i in range(3, n + 1):
    arr[i] = (2 * arr[i - 1] + arr[i - 2]) % 9901

print(arr[n])

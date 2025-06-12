import sys

n = int(sys.stdin.readline())

arr = [1, 3]

for i in range(2, n + 1):
    arr.append(arr[i - 1] + 2 * arr[i - 2])

print(arr[n - 1] % 10007)

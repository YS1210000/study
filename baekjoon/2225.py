import sys

n, k = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(n + 1)] for _ in range(k + 1)]

for i in range(1, k+1):
    arr[i][1] = i
    for j in range(1, n+1):
        arr[i][j] = max(arr[i][j], arr[i - 1][j] + arr[i][j-1])

print(arr[k][n] % 1000000000)

import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
table = [arr[0]] + [[1000001 for _ in range(3)] for _ in range(n-1)]

for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            table[i][k] = min(table[i][k], table[i - 1][j] + arr[i][k])

print(min(table[-1]))

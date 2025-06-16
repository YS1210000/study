import sys

n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))

table = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for start in range(0, i):
        end = i - start
        table[i] = max(table[i], table[start] + table[end])

    table[i] = max(table[i], arr[i])

print(table[-1])

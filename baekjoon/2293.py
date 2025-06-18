import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

table = [1] + [0 for _ in range(k)]

for i in arr:
    for j in range(i, k+1):
        table[j] += table[j-i]

print(table[-1])

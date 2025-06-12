import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

table = [0 for _ in range(1001)]

for i in arr:
    for j in range(i, 0, -1):
        if table[j] == 0:
            continue

        table[i] = max(table[i], table[j] + 1)

    if table[i] == 0:
        table[i] = 1

print(max(table))

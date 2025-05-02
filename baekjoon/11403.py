import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][i] and arr[i][k]:
                arr[j][k] = 1

for text in arr:
    print(' '.join(map(str, text)))

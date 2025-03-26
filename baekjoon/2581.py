import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

arr = [True for _ in range(N+1)]
arr[0] = False
arr[1] = False

for i in range(2, int(N**0.5)+1):
    if arr[i] is True:
        j = 2
        while i*j <= N:
            arr[i*j] = False
            j += 1

result = []

for i in range(M, N+1):
    if arr[i] is True:
        result.append(i)

if len(result) > 0:
    print(sum(result))
    print(result[0])
else:
    print(-1)

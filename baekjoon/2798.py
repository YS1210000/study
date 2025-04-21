import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

result = -sys.maxsize

for i in range(N):
    for j in range(i, N):
        for k in range(j, N):
            if i != j != k:
                tmp = arr[i] + arr[j] + arr[k]
                if tmp <= M and abs(M - tmp) < abs(M - result):
                    result = tmp
                    #print(tmp)

print(result)

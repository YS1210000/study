import sys

n = int(sys.stdin.readline())
arr = [0]+list(map(int, sys.stdin.readline().split()))

result = [0 for _ in range(n)]

for i in range(1, n+1):
    count = 0
    for j in range(n):
        if count == arr[i] and result[j] == 0:
            result[j] = i
            break
        elif result[j] == 0:
            count += 1

print(" ".join(map(str, result)))

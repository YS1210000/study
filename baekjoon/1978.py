import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

for i in arr:
    check = False
    if i > 2:
        for j in range(i//2+1, 1, -1):
            if i % j == 0:
                check = True
                break

        if check is False:
            result += 1
    elif i == 2:
        result += 1


print(result)

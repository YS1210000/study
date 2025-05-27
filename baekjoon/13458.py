import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

result = 0
for i in arr:
    i -= b
    ans = 1

    if i > 0:
        ans += int(i / c)
        i = i % c
        if i != 0:
            ans += 1

    result += ans

print(result)

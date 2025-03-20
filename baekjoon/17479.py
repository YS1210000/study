import sys

H, W = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, W - 1):
    left = max(block[:i])
    right = max(block[i+1:])
    result += max(min(left, right) - block[i], 0)

print(result)

import sys

N = 0
result = -1

for _ in range(10):
    outp, inp = map(int, sys.stdin.readline().split())
    N = N - outp + inp
    result = max(N, result)

print(result)

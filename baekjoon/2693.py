import sys

T = int(sys.stdin.readline())

for _ in range(T):
    A = list(map(int, sys.stdin.readline().split()))

    A.sort(reverse=True)

    print(A[2])

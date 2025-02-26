import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().rstrip().split()))

    max_val = 0
    profit = 0
    for i in range(n-1, -1, -1):
        if days[i] > max_val:
            max_val = days[i]
        else:
            profit += max_val - days[i]

    print(profit)

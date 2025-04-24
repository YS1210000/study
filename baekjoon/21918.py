import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

def turn_switch(a):
    if a == 0:
        return 1
    else:
        return 0

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        arr[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            arr[i] = turn_switch(arr[i])
    elif a == 3:
        for i in range(b-1, c):
            arr[i] = 0
    else:
        for i in range(b-1, c):
            arr[i] = 1

print(" ".join(map(str, arr)))

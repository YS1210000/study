import sys

n = int(sys.stdin.readline())

def search(v, st):
    if v == n:
        print(*st)

    for i in range(1, n+1):
        if i not in st:
            search(v + 1, st + [i])


for i in range(1, n+1):
    search(1, [i])

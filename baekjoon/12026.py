import sys

INF = 1000001
n = int(sys.stdin.readline())
boj = sys.stdin.readline()
table = [INF for _ in range(n)]
table[0] = 0

def check_next(start):
    if boj[start] == "B":
        return "O"
    elif boj[start] == "O":
        return "J"
    else:
        return "B"

start = 0
while start < n:
    if table[start] != INF:
        for i in range(start + 1, n):
            if check_next(start) != boj[i]:
                continue

            table[i] = min(table[i], table[start] + (i - start) ** 2)
    start += 1

if table[-1] != INF:
    print(table[-1])
else:
    print(-1)

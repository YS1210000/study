import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))
volume = {}
table = [[0 for _ in range(M+1)] for _ in range(N+1)]

table[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if table[i-1][j] == 0:
            continue

        nx = j - V[i-1]
        if nx >= 0:
            table[i][nx] += table[i-1][j]

        nx = j + V[i-1]
        if M >= nx:
            table[i][nx] += table[i-1][j]

#for i in table:
#    print(i)

for i in range(M, -1, -1):
    if table[N][i] > 0:
        print(i)
        exit(0)

print(-1)

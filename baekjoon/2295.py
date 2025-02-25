import sys

N = int(input())
U = list()
for i in range(N):
    U.append(int(input()))
U.sort()


xy = set()

for x in U:
    for y in U:
        xy.add(x+y)

for i in range(N-1, -1, -1):
    for j in range(i+1):
        if U[i] - U[j] in xy:
            print(U[i])
            sys.exit(0)

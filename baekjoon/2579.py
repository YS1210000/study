import sys

n = int(sys.stdin.readline())
stair = []
for _ in range(n):
    stair.append(int(sys.stdin.readline()))

if n == 1:
    print(stair[0])
    exit(0)


table = [[0 for _ in range(2)] for _ in range(n)]
table[0][0] = stair[0]
table[1][0] = stair[1]
table[1][1] = stair[0] + stair[1]

for i in range(2, n):
    for j in range(0, 2):
        if j == 0:
            table[i][j] = max(table[i][j], table[i-2][j] + stair[i], table[i-2][j+1] + stair[i])
        else:
            table[i][j] = max(table[i][j], table[i-1][j-1] + stair[i])

        #print(table)

print(max(table[n-1]))

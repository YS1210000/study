import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
table = [[0 for _ in range(n-1)] for _ in range(21)]
table[arr[0]][0] = 1

for i in range(1, n-1):
    for j in range(21):
        if table[j][i-1] == 0:
            continue

        nx = j - arr[i]
        if nx >= 0:
            table[nx][i] += table[j][i-1]

        nx = j + arr[i]
        if 20 >= nx:
            table[nx][i] += table[j][i-1]

print(table[arr[-1]][-1])

'''
for xy in range(21):
    print(table[xy], xy)
'''

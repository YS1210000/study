import sys

strA = [""]+list(sys.stdin.readline().rstrip())
strB = [""]+list(sys.stdin.readline().rstrip())

table = [['' for _ in range(len(strA))] for _ in range(len(strB))]
for i in range(1, len(strA)):
    for j in range(1, len(strB)):
        if strA[i] == strB[j]:
            table[j][i] = table[j-1][i-1] + strA[i]
        else:
            if len(table[j-1][i]) >= len(table[j][i-1]):
                table[j][i] = table[j-1][i]
            else:
                table[j][i] = table[j][i-1]

print(len(table[-1][-1]))
if len(table[-1][-1]) != 0:
    print(table[-1][-1])

import sys

option = []

N = int(sys.stdin.readline())
for _ in range(N):
    option.append(sys.stdin.readline().rstrip())

shortcut = []
result = []


for x in range(N):
    check = option[x]
    arr = [0]

    for i in range(len(check)):
        if check[i] == ' ':
            arr.append(i+1)

    for j in range(len(check)):
        if j not in arr and check[j] != ' ':
            arr.append(j)

    for k in arr:
        if check[k].upper() not in shortcut:
            shortcut.append(check[k].upper())
            check = list(check)
            check.insert(k+1, ']')
            check.insert(k, '[')
            break

    result.append(check)

for i in result:
    print(''.join(i))

import sys

a, p = map(int, sys.stdin.readline().split())
arr = [a]

while True:
    cal = 0

    for i in str(a):
        cal += int(i)**p

    if cal not in arr:
        arr.append(cal)
    else:
        end = arr.index(cal)
        break

    a = cal

print(end)

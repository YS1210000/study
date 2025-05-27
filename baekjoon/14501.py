import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())

    arr.append([t, p])

q = [[0, 0]]

result = -1
while q:
    day, money = q.pop()

    if day < n:
        if day + arr[day][0] < n+1:
            q.append([day + arr[day][0], money + arr[day][1]])
        q.append([day + 1, money])
    else:
        result = max(result, money)

print(result)

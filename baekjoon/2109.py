import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x: (-x[0], x[1]))
#print(arr)

days = [0 for _ in range(10001)]

for reward, limit in arr:
    while limit > 0:
        if days[limit] == 0:
            days[limit] = reward
            break
        limit -= 1

print(sum(days))

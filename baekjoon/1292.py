import sys

start, end = map(int, sys.stdin.readline().split())
arr = [0]
max_n = 1
now = 0

for i in range(1000):
    arr.append(max_n)
    now += 1
    if now == max_n:
        max_n += 1
        now = 0

print(sum(arr[start:end+1]))

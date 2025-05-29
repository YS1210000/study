import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = {}

for _ in range(n):
    arr = list(sys.stdin.readline().rstrip())
    j = len(arr)-1
    for i in arr:
        if i not in dic:
            dic[i] = 10 ** j
        else:
            dic[i] += 10 ** j
        j -= 1

dic = sorted(dic.items(), key=lambda x: -x[1])

start = 9
result = 0
for i, j in dic:
    result += j * start
    start -= 1

print(result)

import sys

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    q.append(tuple(map(int, sys.stdin.readline().split())))

q.sort(key = lambda x:(x[1], x[0]))

use = [0, 0]
answer = 0

for i in q:
    if i[0] >= use[1]:
        answer += 1
        use[1] = i[1]

print(answer)

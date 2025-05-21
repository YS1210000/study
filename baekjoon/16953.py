import sys

now, target = map(int, sys.stdin.readline().split())
answer = []

q = [(now, 1)]
while q:
    v, count = q.pop()

    if v> target:
        continue
    elif v == target:
        answer.append(count)

    v1 = 2 * v
    if v1 <= target:
        q.append((v1, count + 1))

    v2 = 10 * v + 1
    if v2 <= target:
        q.append((v2, count + 1))

if answer:
    print(min(answer))
else:
    print(-1)

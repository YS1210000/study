import sys

N, M = map(int, sys.stdin.readline().split())
unlistened = {}
answer = []

for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    unlistened[tmp] = 1

for _ in range(M):
    tmp = sys.stdin.readline().rstrip()
    if tmp in unlistened:
        answer.append(tmp)

print(len(answer))
answer.sort()
print("\n".join(answer))

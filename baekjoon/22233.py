import sys

N, M = map(int, sys.stdin.readline().split())
dic = {}

for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    if tmp not in dic:
        dic[tmp] = 1

for _ in range(M):
    tmp = sys.stdin.readline().rstrip().split(',')
    for i in tmp:
        if i in dic:
            dic.pop(i)

    print(len(dic))

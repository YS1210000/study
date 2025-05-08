import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n + m + 1)]
dic = {}

for _ in range(n+m):
    p, f, c = map(str, sys.stdin.readline().split())
    if p not in dic:
        dic[p] = []
        dic[p].append([f, c])
    else:
        dic[p].append([f, c])

def search(target, iter):
    if target in dic:
        for i in dic[target]:
            if i[1] == '1':
                search(i[0], iter)
            else:
                iter.append(i[0])
    return iter

q = int(sys.stdin.readline())
for _ in range(q):
    query = list(sys.stdin.readline().rstrip().split('/'))
    target = query[-1]
    result = search(target, [])
    print(len(set(result)), len(result))

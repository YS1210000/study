import sys

dic = {}
size = 0

while True:
    tmp = str(sys.stdin.readline().rstrip())

    if not tmp:
        break

    if tmp not in dic:
        dic[tmp] = 1
    else:
        dic[tmp] += 1

    size += 1

dic = sorted(dic.items(), key = lambda x:x[0])

#print(size, dic)
for k, v in dic:
    ans = round(v /size * 100, 4)
    print(k, '%.4f' %ans)

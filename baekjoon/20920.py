N, M = map(int, input().split())
dic = {}

for i in range(N):
    tmp = input()
    if len(tmp) >= M:
        if tmp in dic:
            dic[tmp] += 1
        else:
            dic[tmp] = 1

result = sorted(dic.items(), key=lambda item:(-item[1], -len(item[0]), item[0]),reverse=False)

for i in result:
    print(i[0])

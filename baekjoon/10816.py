N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))

dic = {}

for i in N_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for target in M_list:
    if target in dic:
        print(dic[target], end=' ')
    else:
        print(0, end=' ')

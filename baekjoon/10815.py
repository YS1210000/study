N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

dic = {}

for i in N_list:
    dic[i] = 1

for j in M_list:
    if j in dic:
        print(1, end=' ')
    else:
        print(0, end=' ')

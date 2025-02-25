N = int(input())
count = 0

tmp = [0 for i in range(1000001)]


for x in range(2, N+1):
    tmp[x] = tmp[x-1]+1
    #print('나누어 떨어지 않아서 -1')
    if x % 2 == 0:
        tmp[x] = min(tmp[x], tmp[x//2]+1)
        #print('2로 나누어 떨어짐')
    if x % 3 == 0:
        tmp[x] = min(tmp[x], tmp[x//3]+1)
        #print('3으로 나누어 떨어짐')

print(tmp[N])

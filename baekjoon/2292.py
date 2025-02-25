#필요한 육각형의 수 1,6,11,16 ...으로 늘어남
#1일때 1개의 방, 2~7일떄 2개의 방, 8~19일때 3개의 방 ...

inc = 1
count = 1

N = int(input())

while N>inc:
    inc += count*6
    count += 1

print(count)

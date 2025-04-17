import sys

N = int(sys.stdin.readline())
now = list(sys.stdin.readline().rstrip())
target = list(sys.stdin.readline().rstrip())

def turn(k):
    if k == '0':
        return '1'
    else:
        return '0'

def click_switch(k, now):
    for i in range(k-1, k+2):
        if 0 <= i < N:
            now[i] = turn(now[i])

def search(now):
    click_count = 0
    for start in range(1, N):
        if now[start-1] != target[start-1]:
            click_switch(start, now)
            click_count += 1
        #print(now)
    if now == target:
        return click_count
    else:
        return sys.maxsize

result = sys.maxsize

now2 = now.copy()
result = min(result, search(now)) #1번째 스위치를 누르지 않은 경우

click_switch(0, now2)
result = min(result, search(now2)+1) #1번째 스위치를 누른 경우

if result < sys.maxsize:
    print(result)
else:
    print(-1)

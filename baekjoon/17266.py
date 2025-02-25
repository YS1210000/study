N = int(input())
M = int(input())
x = list(map(int, input().split()))

def possilbe(H, place):
    if H < place[0] :
        return False
    elif N - place[M-1] > H:
        return False
    for i in range(1, M):
        if place[i] - place[i-1] > H*2:
            return False
    return True

start = 1
end = N

while start <= end:
    mid = (start + end) // 2

    if possilbe(mid, x):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

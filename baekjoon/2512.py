N = int(input())
N_list = list(map(int, input().split()))
M = int(input())

def calculate(N_list, M, x): #x는 정수 상한액 / 사용한 예산의 초과 여부를 return
    result = 0
    for i in N_list:
        if i <= x:
            result += i
        else:
            result += x
    if result > M:
        return False
    else:
        return True

start = 1
end = M

while start <= end:
    mid = (start + end) // 2
    if calculate(N_list, M, mid):
        start = mid + 1
    else:
        end = mid - 1

    #print(start, mid, end)

print(min(max(N_list), end))

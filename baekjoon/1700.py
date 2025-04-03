import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0

q = []

for i in range(K):
    #print(arr[i], q, result)
    if arr[i] not in q: #필요한 플러그가 꽃혀있지 않을 때
        if len(q) < N: #멀티탭에 빈공간이 있을 때
            q.append(arr[i])
        else:
            tmp = q.copy()
            for j in range(i+1, K): #가장 가까운 시일 내에 사용될 플러그를 확인
                if len(tmp) == 1: #가장 이후에 사용될 예정인 플러그만 남은 경우
                    break
                elif arr[j] in tmp:
                    tmp.remove(arr[j])
            q.remove(tmp[-1])
            q.append(arr[i])
            tmp.pop()
            result += 1

print(result)

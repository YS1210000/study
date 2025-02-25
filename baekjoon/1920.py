N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
target = list(map(int, input().split()))

for i in target:
    find = False
    start = 0
    end = len(A)-1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == i:
            find = True
            break
        elif A[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    if find is False:
        print(0)
    else:
        print(1)

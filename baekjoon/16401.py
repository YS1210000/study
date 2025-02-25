M, N = map(int, input().split())
L = list(map(int, input().split()))

start = 1
end = sum(L) // M
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in L:
        count += i // mid

    if count >= M:
        start = mid + 1
    else:
        end = mid - 1

    #print(start, end, count)

print(end)

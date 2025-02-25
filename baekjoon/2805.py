N, M = map(int, input().split())
N_height = sorted(list(map(int, input().split())), reverse=True)

start = 1
end = max(N_height)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in N_height:
        if i <= mid:
            break
        count += i - mid

    if count < M:
        end = mid - 1
    else:
        start = mid + 1

    #print(count, mid, start, end)

print(end)

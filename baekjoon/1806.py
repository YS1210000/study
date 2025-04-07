import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = N-1
mid = 0
sum_val = arr[0]
min_length = sys.maxsize

while start <= end:

    #print(start, mid, sum_val, min_length)

    if sum_val >= S:
        min_length = min(mid - start + 1, min_length)
        sum_val -= arr[start]
        start += 1
        if start > mid:
            mid += 1
            if mid > end:
                break
            else:
                sum_val += arr[mid]

    else:
        mid += 1
        if mid > end:
            break
        else:
            sum_val += arr[mid]

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)

import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = start + k -1
result = sum(arr[start:end+1])

ans = [result]

while end <= n-2:
    result = result - arr[start] + arr[end+1]
    ans.append(result)
    start += 1
    end += 1

print(max(ans))

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

arr = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = 0

counter = [0 for _ in range(200001)]

longest = 0

while end < N:
    counter[arr[end]] += 1
    while counter[arr[end]] > K:
        counter[arr[start]] -= 1
        start += 1
    end += 1
    longest = max(longest, end - start)

print(longest)

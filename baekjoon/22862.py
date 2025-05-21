import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

count_odd = 0
count_even = 0
end = 0
result = 0

for start in range(n):
    while count_odd <= k and end < n:
        if s[end] % 2 == 1:
            count_odd += 1
        else:
            count_even += 1
        end += 1

        if start == 0 and end == n:
            result = count_even
            break

    if count_odd == k + 1:
        result = max(result, count_even)

    if s[start] % 2 == 1:
        count_odd -= 1
    else:
        count_even -= 1

print(result)

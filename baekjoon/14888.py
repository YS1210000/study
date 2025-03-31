import sys

N = int(sys.stdin.readline())
A = list(map(int, (sys.stdin.readline().split())))
add, sub, mul, div = map(int, (sys.stdin.readline().split()))

min_val = sys.maxsize
max_val = -sys.maxsize

def dfs(arr, i):
    global add, sub, mul, div, max_val, min_val
    if i == N:
        max_val = max(max_val, arr)
        min_val = min(min_val, arr)
    else:
        if add > 0:
            add -= 1
            dfs(arr + A[i], i+1)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(arr - A[i], i+1)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(arr * A[i], i+1)
            mul += 1
        if div > 0:
            div -= 1
            dfs(int(arr / A[i]), i+1)
            div += 1

dfs(A[0], 1)

print(max_val)
print(min_val)

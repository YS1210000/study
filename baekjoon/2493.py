import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stack = [[1, arr[0]]]
result = [0]

for i in range(1, N):
    while stack:
        #print(stack)
        if stack[-1][1] >= arr[i]:
            result.append(stack[-1][0])
            stack.append([i + 1, arr[i]])
            break
        else:
            stack.pop()

    if not stack:
        result.append(0)
        stack.append([i + 1, arr[i]])

print(' '.join(map(str, result)))

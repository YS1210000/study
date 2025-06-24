import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

answer = 0
for i in range(n):
    start = 0
    end = n - 1

    while start < end:
        cal = arr[start] + arr[end]
        if cal > arr[i]:
            end -= 1
        elif cal < arr[i]:
            start += 1
        else:
            if start != i and end != i:
                answer += 1
                break
            else:
                if start == i:
                    start += 1
                else:
                    end -= 1

print(answer)

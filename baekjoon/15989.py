import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    result = 0

    for i in range(n//3, -1, -1): #3의 갯수 i
        result += 1 + (n - 3*i) // 2

    print(result)

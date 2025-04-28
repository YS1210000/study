import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    dic = {}

    for _ in range(n):
        name, category = sys.stdin.readline().split()

        if category not in dic:
            dic[category] = 2
        else:
            dic[category] += 1

    result = 1
    for i in dic.values():
        result *= i

    print(result-1)

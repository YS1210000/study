import sys
from collections import deque
from copy import deepcopy

T = int(sys.stdin.readline())

def print_result(result):
    for line in result:
        print(" ".join(map(str, line)))

    return 0

for _ in range(T):
    n, d = map(int, sys.stdin.readline().split())
    d = d // 45 #45도마다 (원소의 개수 / 8)칸이 밀림
    while d < 0:
        d += 8

    arr = []
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    result = deepcopy(arr)

    if d == 0 or d == 8:
        print_result(result)
        continue

    for _ in range(d):
        for i in range(n):
            result[i][n//2] = arr[i][i] # 주대각 -> 세로
            result[i][n - i - 1] = arr[i][n//2] #세로 -> 반대각
            result[n//2][i] = arr[n - i - 1][i] #반대각 -> 가로
            result[i][i] = arr[n//2][i] #가로 -> 주대각

        arr = deepcopy(result)

    print_result(result)

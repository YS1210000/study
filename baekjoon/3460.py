import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    binary = ''
    while N > 0:
        if N % 2 == 0:
            binary += '0'
        else:
            binary += '1'
        N //= 2

    for i in range(0, len(binary)):
        if binary[i] == '1':
            print(i, end=' ')

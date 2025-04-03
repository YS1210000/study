import sys

N, M = map(int, sys.stdin.readline().split())

def tracking(i, output):
    if i == M:
        print(' '.join(map(str, output)))
    else:
        for j in range(1, N+1):
            output.append(j)
            tracking(i+1, output)
            output.pop()

tracking(0, [])

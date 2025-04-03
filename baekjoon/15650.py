import sys

N, M = map(int, sys.stdin.readline().split())
result = []

def tracking(i, output):
    if i == M:
        print(' '.join(map(str, output)))
    else:
        if output:
            start = output[-1]
        else:
            start = 1
        for j in range(start, N+1):
            if j not in output:
                output.append(j)
                tracking(i + 1, output)
                output.pop()

tracking(0, [])

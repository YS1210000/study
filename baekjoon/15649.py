import sys

N, M = map(int, sys.stdin.readline().split())

def output(i, visited):
    global N, M
    if i == M:
        print(' '.join(map(str, visited)))
    else:
        for j in range(1, N+1):
            if j not in visited:
                visited.append(j)
                output(i + 1, visited)
                visited.pop()

output(0, [])

import sys

N = int(sys.stdin.readline())

def checkblock(i, visited):
    for k in range(i):
        if visited[i] == visited[k] or abs(visited[i] - visited[k]) == abs(i - k):
            return False

    return True

def count(i, visited):
    global result
    if i == N:
        result += 1
    else:
        for j in range(N):
            visited[i] = j
            if checkblock(i, visited):
                count(i + 1, visited)

result = 0
count(0, [0 for _ in range(N)])
print(result)

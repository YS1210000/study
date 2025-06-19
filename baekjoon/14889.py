import itertools
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

search = list(itertools.combinations([i for i in range(n)], n // 2))

start = 0
end = len(search) - 1

ans = sys.maxsize

while start < end:
    A = search[start]
    B = search[end]

    Ascore = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            Ascore += arr[A[i]][A[j]]
            Ascore += arr[A[j]][A[i]]

    Bscore = 0
    for i in range(len(B)):
        for j in range(i + 1, len(B)):
            Bscore += arr[B[i]][B[j]]
            Bscore += arr[B[j]][B[i]]

    ans = min(ans, abs(Ascore - Bscore))

    start += 1
    end -= 1

print(ans)

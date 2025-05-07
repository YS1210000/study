import sys

n = int(sys.stdin.readline())
arr = []
size = 0

for _ in range(n):
    s = tuple(map(int, sys.stdin.readline().split()))
    arr.append(s)
    size = max(size, s[1])

#arr.sort(key=lambda x: (x[0], -x[1]))

paper = [0 for _ in range(size+1)]
for i in arr:
    for j in range(i[0], i[1]+1):
        paper[j] += 1

start = 0
height = 0
width = 0
answer = 0
paper.append(0)
while start <= size+1:
    if paper[start] == 0:
        answer += height * width
        height = 0
        width = 0
    else:
        height = max(height, paper[start])
        width += 1
    start += 1

print(answer)

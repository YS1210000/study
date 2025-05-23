import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = []
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    apple.append((a-1, b-1))

l = int(sys.stdin.readline())
move = []
for _ in range(l):
    x, c = sys.stdin.readline().split()
    move.append((int(x), c))

body = deque()
head = [0, 0]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)] #0번 - 오른쪽을 향할 때
second = 0
start = 0

dir = 0

while True:
    if start < len(move) and move[start][0] == second:
        if move[start][1] == "L":
            dir -= 1
            if dir < 0:
                dir = 3
        elif move[start][1] == "D":
            dir += 1
            if dir > 3:
                dir = 0
        start += 1
        #print("turn")

    second += 1

    head_x = head[0] + d[dir][0]
    head_y = head[1] + d[dir][1]

    if head_y < 0 or head_y >= n or head_x < 0 or head_x >= n: #벽에 부딪히는 경우
        print(second)
        exit(0)

    for x, y in body:
        if head_x == x and head_y == y: #몸에 부딪히는 경우
            print(second)
            exit(0)

    incre_body = False
    for i in range(len(apple)):
        y, x = apple[i]
        if head_x == x and head_y == y: #사과가 있는 경우
            incre_body = True
            del apple[i]
            break

    body.append(head)
    if not incre_body: #사과를 먹지 않은 경우 몸 길이가 늘어나지 않음
        body.popleft()

    head = [head_x, head_y]


    '''
    print(head, body)
    for x in range(n):
        for y in range(n):
            if [y, x] == head:
                print("★", end="")
            elif [y, x] in body:
                print("■", end="")
            elif (x, y) in apple:
                print("●", end="")
            else:
                print("□", end="")
        print()
    print("now : ", second)
    '''

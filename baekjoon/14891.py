import sys
from collections import deque

gear = deque()
for _ in range(4):
    gear.append(deque(map(int, sys.stdin.readline().rstrip())))

k = int(sys.stdin.readline())
for _ in range(k):
    num, dir = map(int, sys.stdin.readline().split())

    q = [0, 0, 0, 0]

    tmp_dir = dir
    q[num - 1] = dir
    for gear_num in range(num - 2, -1, -1): #회전한 톱니바퀴의 왼쪽을 회전
        if gear[gear_num+1][6] == gear[gear_num][2]:
            break
        tmp_dir *= -1

        q[gear_num] = tmp_dir

    tmp_dir = dir
    for gear_num in range(num, 4): #회전한 톱니바퀴의 오른쪽을 회전
        if gear[gear_num-1][2] == gear[gear_num][6]:
            break
        tmp_dir *= -1

        q[gear_num] = tmp_dir

    for i in range(4):
        gear[i].rotate(q[i])
    #print(q)
    #print(gear)

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2**i

print(answer)

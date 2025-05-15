import sys

p, m = map(int, sys.stdin.readline().split())

room = []
for _ in range(p):
    level, name = sys.stdin.readline().split()
    level = int(level)

    isempty = True
    #print(room)
    for i in range(len(room)):
        leader_level, leader_name = room[i][0]
        if len(room[i]) < m and leader_level - 10 <= level <= leader_level + 10:
            room[i].append((level, name))
            isempty = False

            break

    if isempty is True: #방 만들기
        room.append([(level, name)])

for i in room:
    i.sort(key=lambda x: x[1])
    if len(i) == m:
        print("Started!")
        for j in i:
            print(j[0], j[1])
    else:
        print("Waiting!")
        for j in i:
            print(j[0], j[1])

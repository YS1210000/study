import sys

string1 = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
string2 = []

for _ in range(M):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'L':
        if string1:
            string2.append(string1.pop())
    elif order[0] == 'D':
        if string2:
            string1.append(string2.pop())
    elif order[0] == 'B':
        if string1:
            string1.pop()
    elif order[0] == 'P':
        string1.append(order[1])


string1.extend(reversed(string2))
print(''.join(string1))

''' 시간 초과
string = list(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
cursor = len(string)


for _ in range(M):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == 'P':
        string.insert(cursor, order[1])
        cursor += 1
    elif cursor > 0 and order[0] == 'L':
        cursor -= 1
    elif cursor < len(string) and order[0] == 'D':
        cursor += 1
    elif 0 < cursor and order[0] == 'B':
        del string[cursor-1]
        cursor -= 1
    #print(string, cursor)

for i in string:
    print(i, end='')
'''

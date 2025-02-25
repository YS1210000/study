import sys

S = set()

M = int(input())

order = [0, 0]

for i in range(M):
    order = sys.stdin.readline().strip().split()

    if len(order) != 1 and order[1] != 0:
        order[1] = int(order[1])

    if order[0] == 'add':
        S.add(order[1])
    elif order[0] == 'remove':
        S.discard(order[1])
    elif order[0] == 'check':
        if order[1] in S:
            print("1")
        else:
            print("0")
    elif order[0] == 'toggle':
        if order[1] in S:
            S.discard(order[1])
        else:
            S.add(order[1])
    elif order[0] == 'all':
        S = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif order[0] == 'empty':
        S.clear()



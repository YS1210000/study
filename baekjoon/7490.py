import sys

T = int(sys.stdin.readline())

def DFS(top, N, result):
    global q
    if top == N:
        q.append(result)
    else:
        top += 1
        for i in range(3):
            if i == 0:
                tmp = result + " " + str(top)
            elif i == 1:
                tmp = result + "+" + str(top)
            elif i == 2:
                tmp = result + "-" + str(top)
            DFS(top, N, tmp)

for _ in range(T):
    q = []
    N = int(sys.stdin.readline())

    result = '1'
    DFS(1, N, result)
    #print(q)

    for i in q:
        if eval(i.replace(" ","")) == 0:
            print(i)

    print()

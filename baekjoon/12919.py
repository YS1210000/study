import sys

# S -> T 는 경우의 수가 너무 많아지므로 T -> S를 찾으면 해결 가능
# 마지막이 A면 A를 제거 / 처음이 B면 B를 제거하고 뒤집기

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

Q = [T]

while Q:
    text = Q.pop()
    #print(text)
    if text == S:
        print(1)
        sys.exit(0)

    if len(text) > 0:
        if text[-1] == 'A':
            Q.append(text[:-1])
        if text[0] == 'B':
            Q.append(text[1:][::-1])

    #print(Q)

print(0)

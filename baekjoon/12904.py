import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()

def search(t):
    if t[-1] == "B":
        t = t[::-1]
        t = t[1:]
    else:
        t = t[:-1]
    return t

while len(t) > len(s):
    t = search(t)
    #print(t)

if t == s:
    print(1)
else:
    print(0)

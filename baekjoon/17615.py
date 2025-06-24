import sys

n = int(sys.stdin.readline())
arr = sys.stdin.readline().rstrip()

def check_ball(color):
    for i in range(n):
        if arr[i] != color:
            break

    for j in range(n-1, -1, -1):
        if arr[j] != color:
            break

    #print(arr[i:])
    #print(arr[:j+1])
    return min(arr[i:].count(color), arr[:j+1].count(color))

print(min(check_ball("R"), check_ball("B")))

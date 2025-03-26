import sys

a, b = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t = gcd(a, b)
print(t)
print(a * b // t)

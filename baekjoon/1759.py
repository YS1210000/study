import sys
import itertools

l, c = map(int, sys.stdin.readline().split())
arr = list(map(str, sys.stdin.readline().split()))
check_mo = ['a', 'e', 'i', 'o', 'u']
mo = []
ja = []

for i in arr:
    if i in check_mo:
        mo.append(i)
    else:
        ja.append(i)

result = []
for m in range(1, l-1):
    j = l - m
    a = list(itertools.combinations(mo, m))
    b = list(itertools.combinations(ja, j))

    for n1 in a:
        for n2 in b:
            string = list(n1 + n2)
            string.sort()
            result.append("".join(string))

print("\n".join(sorted(result)))

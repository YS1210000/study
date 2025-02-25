A, B = map(int, input().split())
Aset = set(map(int, input().split()))
Bset = set(map(int, input().split()))

result = sorted(list(Aset - Bset))

print(len(result))
for i in result:
    print(i,end=' ')

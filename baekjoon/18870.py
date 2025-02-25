N = int(input())
X = list(map(int, input().split()))

Xprime = sorted(X)

#print(Xprime)

dic = {}

count = 0
for i in Xprime:
    if i not in dic:
        dic[i] = count
        count += 1

for i in X:
    print(dic[i], end=' ')

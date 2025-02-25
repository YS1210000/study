N =int(input())

people = []
for i in range(N):
    x, y = map(int, input().split())
    people.append([x, y])

rank = []

for j in range(N):
    count = 1
    for k in range(N):
        if people[k][0] > people[j][0] and people[k][1] > people[j][1]:
            count += 1
    rank.append(count)

for l in rank:
    print(l, end=" ")

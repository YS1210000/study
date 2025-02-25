
N, Game = map(str, input().split())
Users = 0

if Game == 'Y':
    Users = 2
elif Game == 'F':
    Users = 3
elif Game == 'O':
    Users = 4

people = set()

for i in range(int(N)):
    people.add(input())

#print(people)

print(len(people)//(Users-1))

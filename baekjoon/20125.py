
N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

First = False
heart = []

for i in range(N):
    M = input()
    for j in range(N):
        if M[j] == '*':
            if First == False:
                First = True
                heart.append([i+1,j])
            arr[i][j] = 1

print(f"{heart[0][0]+1} {heart[0][1]+1}")

count = 0
for left_arm in range(0, heart[0][1]):
    if arr[heart[0][0]][left_arm] == 1:
        count += 1
print(count, end=' ')

count = 0
for right_arm in range(heart[0][1]+1, N):
    if arr[heart[0][0]][right_arm] == 1:
        count += 1
print(count, end=' ')

count = 0
for core in range(heart[0][0]+1, N):
    if arr[core][heart[0][1]] == 1:
        #print(heart[0][1], core)
        count += 1
print(count, end=' ')

leg_col = heart[0][0]+1+count

count = 0
for left_leg in range(leg_col, N):
    if arr[left_leg][heart[0][1]-1] == 1:
        #print(heart[0][1], core)
        count += 1
print(count, end=' ')

count = 0
for right_leg in range(leg_col, N):
    if arr[right_leg][heart[0][1]+1] == 1:
        #print(heart[0][1], core)
        count += 1
print(count, end=' ')

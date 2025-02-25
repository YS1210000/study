N = int(input())
arr = list(map(int, input().split()))

studentN = int(input())

def TurnSwitch(V):
    if V == 1:
        return 0
    else:
        return 1

for i in range(studentN):
    sex, switch_num = map(int, input().split())

    if sex == 1: #남학생
        for i in range(switch_num, N+1, switch_num):
            arr[i-1] = TurnSwitch(arr[i-1])
    else: #여학생
        switch_num -= 1
        left = switch_num
        right = switch_num

        while left > 0 and right < N-1 and arr[left - 1] == arr[right + 1]:
            left -= 1
            right += 1

        for i in range(left, right+1):
            arr[i] = TurnSwitch(arr[i])


    #print(arr)

count = 0
for i in arr:
    if(count % 20 == 0 and count != 0):
        print()
    print(i, end=' ')
    count += 1

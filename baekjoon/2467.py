N = int(input())
N_list = list(map(int, input().split()))

start = 0
end = N-1


answer = abs(N_list[start] + N_list[end])
x = start
y = end

while start < end:
    tmp = N_list[start] + N_list[end]


    if answer > abs(tmp):
        x = start
        y = end
        answer = abs(tmp)
        #print(x, y)

        if answer == 0:
            break

    if tmp < 0:
        start += 1
    else:
        end -= 1

print(N_list[x], N_list[y])

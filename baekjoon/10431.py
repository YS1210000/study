
P = int(input())

for i in range(P):
    result = 0
    line = list(map(int, input().split()))

    case_num = line.pop(0)

    new_line = [line.pop(0)]

    while line:
        people = line.pop(0)
        frt_people = 0

        for i in new_line:
            if i > people:
                frt_people = i
                break

        if frt_people == 0: #맨 뒤에 서야할 경우
            new_line.append(people)
        else:
            #print("낄자리",frt_people, new_line.index(frt_people)) #낄자리
            result += len(new_line) - new_line.index(frt_people)
            new_line.insert(new_line.index(frt_people), people)
        #print(new_line)

    print(case_num, result)

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    tmp = list(map(int, sys.stdin.readline().split()))
    arr = [[] for _ in range(min(n, 201))]
    count_people = [0 for _ in range(min(n, 201))]

    first_score = sys.maxsize
    same_team = []

    for i in range(n): #각 팀의 인원수 확인
        count_people[tmp[i]] += 1

    counter = 1
    for i in range(n):
        if count_people[tmp[i]] == 6: #인원수가 6명일 경우에만 점수를 계산할 예정
            arr[tmp[i]-1].append(counter)
            counter += 1

    for i in range(len(arr)):
        if len(arr[i]) != 6:
            continue

        tmp = sum(arr[i][0:4]) #상위 4명의 점수 합

        if tmp < first_score: #합산 점수가 가장 낮은 팀을 저장
            first_score = tmp
            same_team = [i]
        elif tmp == first_score: #중복 점수인 팀을 저장
            same_team.append(i)

    if len(same_team) == 1:
        print(same_team[0]+1)
    else:
        fifth_score = sys.maxsize
        for i in same_team:
            if arr[i][4] < fifth_score:
                fifth_score = arr[i][4]
                winner = i
        print(winner+1)

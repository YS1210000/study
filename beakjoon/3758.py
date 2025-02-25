T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split()) # 팀 개수 n, 문제 개수 k, 나의 팀 id t, 로그 엔트리의 수 m
    count = [0 for i in range(n)] #각 팀이 제출한 횟수
    last = [-1 for i in range(n)] #각 팀의 마지막으로 제출한 번호
    score = [] #각 팀의 점수

    for time in range(m):
        i, j, s = map(int, input().split()) #팀 id i, 문제 번호 j, 획득한 점수 s, 제출 순서 반영
        count[i-1] += 1
        last[i-1] = time
        score.append([i, j, s])

    score.sort(key=lambda x: (x[0], x[1], -x[2]))


    grade = [0 for i in range(n)]
    last_id = -1
    last_qid = -1
    for i, j, s in score:
        if i != last_id:
            last_id = i
            last_qid = j
            grade[i-1] = s
        elif j != last_qid:
            last_qid = j
            grade[i-1] += s


    answer = []

    for i in range(n):
        answer.append([i, grade[i], count[i], last[i]])

    answer.sort(key=lambda x: (-x[1], x[2], x[3]))

    #print(answer)

    for j in range(n):
        if answer[j][0] == t-1:
            print(j+1)
            break




    #1.점수가 다른지 확인
    #2.점수가 같은 경우 풀이를 제출한 횟수를 확인
    #3.둘 다 같은 경우 마지막 제출 시간을 확인
    #나의 팀의 등수를 출력







    #print(count, last, score)

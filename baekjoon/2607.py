import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    arr.append(sys.stdin.readline().rstrip())

def check_alphabet(word):
    tmp = {}
    for i in word:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    return tmp

result = 0
for i in range(1, n):
    word = check_alphabet(arr[0])

    count = 0
    for j in arr[i]:
        if j in word:
            word[j] -= 1
        else:
            word[j] = -1

    before = 0
    isfail = False
    ischange = False
    for k in word.values():
        if k == 0:
            continue
        elif k > 1 or k < -1: #2개 이상의 문자가 다를 때
            isfail = True
            break #이 아래로는 항상 문자가 1개만 차이나는 경우임
        elif ischange and k != 0: #문자를 이미 변환하였는데 또 갯수가 일치하지 않는 문자가 출현
            isfail = True
            break
        elif before == 0: #k가 1 혹은 -1(1개의 문자만 다름)
            before = k #1)문자를 추가, 혹은 삭제로 해결 2)문자를 변환하여 해결
        elif before == -k: #문자를 변환하여 해결
            ischange = True
        else: #문자가 2개이상 모자라거나 많은 경우
            isfail = True
            break

    if not isfail:
        result += 1
print(result)

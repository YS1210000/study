

sentence = ''


ja = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
mo = ['a', 'e', 'i', 'o' ,'u']

while True:
    sentence = input()
    if sentence == 'end':
        break

    prev = ''
    aeiou = False #조건1
    sequn_chk = False #조건2 - 모/자 구분
    sequn = 0 #조건2 - 연속성 체크
    now_jamo = False
    fail = False

    for i in sentence:
        if i in mo:
            now_jamo = False #모음일 경우 False
        else:
            now_jamo = True

        if aeiou == False and now_jamo == False: #조건1
            aeiou = True

        if now_jamo == False and sequn_chk == False: #현재 모음, 이전 모음일 경우 연속성 +1
            sequn += 1
        elif now_jamo == True and sequn_chk == True: #현재 자음, 이전 자음일 경우 연속성 +1
            sequn += 1
        else:
            sequn = 1

        if sequn == 3: #조건2 - 모음이 3개 혹은 자음이 3개 연속일 경우
            fail = True
            break

        if prev == i: #조건3 - 같은 글자가 연속적일 경우, 단 ee와 oo는 예외
            if i != 'e' and i != 'o':
                fail = True
                break

        prev = i
        if now_jamo is False: #현재 모음, 이전 모음일 경우 연속성 +1
            sequn_chk = False
        else:
            sequn_chk = True

        #print(f"{i}, {sequn}")

    if aeiou is False: #조건 1 - 모음을 포함하지 않았을경우
        fail = True

    if fail is True:
        print(f'<{sentence}> is not acceptable.')
    else:
        print(f'<{sentence}> is acceptable.')

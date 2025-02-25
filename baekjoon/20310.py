s = list(input())

zero = s.count('0') // 2
one = s.count('1') // 2

#1은 앞에서부터 삭제
#0은 뒤에서부터 삭제

slider = len(s)-1
while zero > 0:
    if s[slider] == '0':
        del s[slider]
        zero -= 1
    slider -= 1
    #print(slider, zero)

slider2 = 0
while one > 0:
    if s[slider2] == '1':
        del s[slider2]
        one -= 1
    else:
        slider2 += 1
    #print(slider2, one)

for i in s:
    print(i, end='')

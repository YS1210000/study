import sys

A = list(sys.stdin.readline().rstrip())
dic = {}

for i in sorted(A):
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

odd_num = 0
even_num = 0

for k in dic.values():
    if k % 2 == 0:
        even_num += 1
    else:
        odd_num += 1

if len(A) % 2 == 0: #문자열이 짝수개 -> 모든 문자가 짝수여야함
    if odd_num != 0:
        print("I'm Sorry Hansoo")
        exit(0)
else: #문자열이 홀수개 -> 1개의 문자만 홀수여야함
    if odd_num != 1:
        print("I'm Sorry Hansoo")
        exit(0)

front = ""
mid = ""
back = ""

for st, co in dic.items():
    while co > 0:
        if co == 1:
            mid += st
            co = 0
        else:
            front += st
            back += st
            co -= 2

print(front+mid+back[::-1])

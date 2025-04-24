import sys

S = sys.stdin.readline()
result = ""

ans_num = []
blank = []
isclose = False

start = 0
for i in range(0, len(S)):
    if S[i] == "<":
        ans_num.append((start, i, -1))
        start = i
        isclose = True
    elif S[i] == ">":
        ans_num.append((start, i+1, 0))
        start = i+1
        isclose = False
    elif S[i] == " " and isclose is False:
        ans_num.append((start, i, -1))
        start = i
        blank.append(i)
ans_num.append((start, len(S), -1))

for start, end, backward in ans_num:
    if backward == -1:
        tmp = S[start:end]
        tmp = tmp.replace(" ","")
        tmp = tmp.replace("\n","")
        result += tmp[::-1]
    else:
        result += S[start:end]

result = list(result)

for i in blank:
    result.insert(i, " ")

#print(ans_num)
print("".join(result))

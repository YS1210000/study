import sys

sentence = sys.stdin.readline().strip()

before = ""
arr = []
for i in sentence:
    if i == "+":
        arr.append(int(before))
        before = ""
        arr.append("+")
    elif i == "-":
        arr.append(int(before))
        before = ""
        arr.append("-")
    else:
        before += i
arr.append(int(before))

result = arr[0]
minus = False
counting_sum = 0

i = 1
while i < len(arr):
    #print(i)
    if arr[i] == "-":
        minus = True
        result -= counting_sum + arr[i + 1]
        i += 1
        counting_sum = 0
    elif arr[i] == "+" and minus is False:
        result += arr[i + 1]
        i += 1
    elif arr[i] == "+" and minus is True:
        counting_sum += arr[i + 1]
        i += 1
    else:
        counting_sum += arr[i]
    i += 1

print(result-counting_sum)

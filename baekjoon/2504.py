import sys

question = list(sys.stdin.readline())
stack = []
result = 0
continued = 1

for i in range(len(question)):
    #print(stack, result, continued)
    if question[i] == '(':
        stack.append(question[i])
        continued *= 2

    elif question[i] == '[':
        stack.append(question[i])
        continued *= 3

    elif question[i] == ')':
        if not stack or stack[-1] == "[":
            print(0)
            exit(0)
        stack.pop()
        if question[i-1] == "(":
            result += continued
        continued //= 2

    elif question[i] == ']':
        if not stack or stack[-1] == "(":
            print(0)
            exit(0)
        stack.pop()
        if question[i-1] == "[":
            result += continued
        continued //= 3

if stack:
    print(0)
else:
    print(result)

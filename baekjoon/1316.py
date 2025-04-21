import sys

N = int(sys.stdin.readline())
result = 0

for _ in range(N):
    word = sys.stdin.readline()

    check = {}
    is_con_word = True

    before_word = ""
    for i in word:
        if i in check:
            if before_word != i:
                is_con_word = False
                break
        else:
            check[i] = 1

        before_word = i

    if is_con_word is True:
        result += 1

print(result)

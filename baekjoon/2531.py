import sys
from collections import deque

N, d, k, c = map(int, sys.stdin.readline().split())

sushi = deque([])
max_type = []
now_type = -1


for _ in range(k-1):
    tmp = int(sys.stdin.readline().rstrip())
    sushi.append(tmp)

repeat_part = list(sushi)

for _ in range(N-k+1):
    tmp = int(sys.stdin.readline().rstrip())

    if len(sushi) < k:
        sushi.append(tmp)
    else:
        sushi.popleft()
        sushi.append(tmp)

    input_sushi = set(sushi)

    if c in input_sushi:
        input_sushi.remove(c)

    if len(input_sushi) > now_type:
        now_type = len(input_sushi)
        max_type.clear()
        max_type.append(list(sushi))
    elif len(input_sushi) == now_type:
        now_type = len(input_sushi)
        max_type.append(list(sushi))

    #print(sushi, input_sushi)

for i in repeat_part:
    sushi.popleft()
    sushi.append(i)

    input_sushi = set(sushi)

    if c in input_sushi:
        input_sushi.remove(c)

    if len(input_sushi) > now_type:
        now_type = len(input_sushi)
        max_type.clear()
        max_type.append(list(sushi))
    elif len(input_sushi) == now_type:
        now_type = len(input_sushi)
        max_type.append(list(sushi))


result = -1
#print(max_type)

for i in max_type:
    #print(i)
    counter = len(set(i))
    if c not in i:
        counter += 1

    result = max(result, counter)

print(result)

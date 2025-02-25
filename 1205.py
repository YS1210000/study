N, new_score, P = map(int, input().split())

if N == 0:
    arr = []
else:
    arr = list(map(int, input().split()))

place = -1

for i in range(N):
    if arr[i] <= new_score:
        place = i
        break

if place == -1: #등수가 맨 뒤
    if len(arr) + 1 <= P:
        print(len(arr) + 1)
    else:
        print(-1)
else:
    if place + arr.count(new_score) + 1 <= P:
        print(place + 1)
    else:
        print(-1)

N, X = map(int, input().split())
days = list(map(int, input().split()))

slider = sum(days[0:X])
before = slider
conti = 1
top = slider
top_conti = 1

for i in range(X, N):
    slider += days[i]
    slider -= days[i-X]
    #print(slider)

    if slider == top:
        top_conti += 1
    elif slider > top:
        top = slider
        top_conti = 1

if top == 0:
    print("SAD")
else:
    print(top)
    print(top_conti)

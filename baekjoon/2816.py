N = int(input())
channels = []

for i in range(N):
    channels.append(input())

def Button(a, b):
    return b, a


slider = 0
now_sort = 0

while True:
    KBS1_d = channels.index("KBS1")
    KBS2_d = channels.index("KBS2")

    if KBS1_d == 0 and KBS2_d == 1:
        break

    if KBS1_d != 0:
        if slider < KBS1_d:
            slider += 1
            print("1",end='')
        elif slider > KBS1_d:
            slider -= 1
            print("2",end='')
        else:
            slider -= 1
            channels[KBS1_d], channels[KBS1_d - 1] = Button(channels[KBS1_d], channels[KBS1_d - 1])
            KBS1_d -= 1
            print("4",end='')
    else:
        if slider < KBS2_d:
            slider += 1
            print("1",end='')
        elif slider > KBS2_d:
            slider -= 1
            print("2",end='')
        else:
            slider -= 1
            channels[KBS2_d], channels[KBS2_d - 1] = Button(channels[KBS2_d], channels[KBS2_d - 1])
            KBS2_d -= 1
            print("4",end='')




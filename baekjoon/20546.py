import sys

Jcash = int(sys.stdin.readline())
Scash = Jcash
stock = list(map(int, sys.stdin.readline().split()))
Jstock = 0
Sstock = 0

stock_con_incre = 0
stock_con_decre = 0
last_stock_price = stock[-1]

for stock_price in stock:
    if Jcash >= stock_price:
        Jstock += Jcash // stock_price
        Jcash %= stock_price

    if stock_price > last_stock_price:
        stock_con_incre += 1
        stock_con_decre = 0
    elif stock_price < last_stock_price:
        stock_con_incre = 0
        stock_con_decre += 1
    else:
        stock_con_incre = 0
        stock_con_decre = 0

    if stock_con_incre >= 3:
        Scash += Sstock * stock_price
        Sstock = 0
        #print(f"now price:{stock_price}, 성민 매도")

    if stock_con_decre >= 3:
        Sstock += Scash // stock_price
        Scash %= stock_price
        #print(f"now price:{stock_price}, 성민 매수")

    last_stock_price = stock_price

    #print(f"now price:{stock_price}, 준현:{Jstock}주 보유, 남은 자산:{Jcash} / 성민:{Sstock}주 보유, 남은 자산:{Scash}")

Jlast = Jstock * stock[-1] + Jcash
Slast = Sstock * stock[-1] + Scash

if Jlast > Slast:
    print("BNP")
elif Jlast < Slast:
    print("TIMING")
else:
    print("SAMESAME")

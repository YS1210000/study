
while True:
    A, B, C = map(int, input().split())

    if A == B == C:
        if A == 0:
            break
        else:
            print("Equilateral")
    elif A + B <= C or A + C <= B or B + C <= A:
        print("Invalid")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")

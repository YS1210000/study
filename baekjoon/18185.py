N = int(input())
A = list(map(int, input().split()))

slider = 0
cost = 0

while slider < N:
    if A[slider] > 0:
        if slider < N-2 and A[slider+1] > A[slider+2]:
            minval = min(A[slider], A[slider+1] - A[slider+2])
            A[slider] -= minval
            A[slider+1] -= minval
            cost += minval * 5

        if slider < N-2 and A[slider+1] > 0 and A[slider+2] > 0:
            minval = min(A[slider], A[slider+1], A[slider+2])
            A[slider] -= minval
            A[slider+1] -= minval
            A[slider+2] -= minval
            cost += minval * 7

        elif slider < N-1 and A[slider+1] > 0:
            minval = min(A[slider], A[slider+1])
            A[slider] -= minval
            A[slider+1] -= minval
            cost += minval * 5

        cost += A[slider] * 3
        A[slider] = 0

    slider += 1

print(cost)

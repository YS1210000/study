import sys

S = int(sys.stdin.readline())

sum_num = 0
iter = 0

while sum_num <= S:
    iter += 1
    sum_num += iter
    #print(iter, sum_num)

print(iter-1)

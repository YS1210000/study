import sys

N = int(sys.stdin.readline().rstrip())
col = []

for _ in range(N):
    L, H = map(int, sys.stdin.readline().rstrip().split())
    col.append([L, H])

col.sort()
#print(col)

top = sorted(col, key=lambda x: -x[1])[0]
top_idx = col.index(top)
#top[0]이 top_idx, top[1]이 top_height

left = 0
right = N-1
left_area = 0
right_area = 0

last_left_roof = -1
last_right_roof = -1

while left < top_idx:
    left_roof = max(last_left_roof, col[left][1])
    left_area += (col[left+1][0] - col[left][0]) * left_roof
    left += 1
    last_left_roof = left_roof

while right > top_idx:
    right_roof = max(last_right_roof, col[right][1])
    right_area += (col[right][0] - col[right-1][0]) * right_roof
    right -= 1
    last_right_roof = right_roof


#area += col[left][1]

print(left_area + right_area + top[1])

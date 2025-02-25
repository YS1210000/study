
H, W, N, M = map(int, input().split())

# H가 행의 수, W가 열의 수
# N이 세로, M이 가로

x = H//(N+1)
y = W//(M+1)

if H % (N+1) != 0:
    x += 1
if W % (M+1) != 0:
    y += 1





print(x*y)

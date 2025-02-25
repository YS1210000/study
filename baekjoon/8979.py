
N, K = map(int, input().split())
medals =[]

for i in range(N):
    medals.append(list(map(int, input().split())))

medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

for j in range(N):
    if medals[j][0] == K:
        idx = j

for k in range(N):
    if medals[idx][1:] == medals[k][1:]:
        print(k+1)
        break


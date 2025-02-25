N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

answer = []

def DFS(matrix, V, result, arr): #arr은 -1, 0, 1만
    result += matrix[V[0]][V[1]]
    na = [-1, 0, 1]
    if arr in na:
        na.remove(arr)

    #print(V, result, na)

    if V[0] >= N-1:
        return answer.append(result)
    else:
        V[0] += 1
        for i in na:
            tmp = V[1] + i
            # print(V)
            if tmp > -1 and tmp < M:
                DFS(matrix, [V[0], tmp], result, i)


for i in range(0, M):
    DFS(matrix, [0,i], 0, 2)
print(min(answer))

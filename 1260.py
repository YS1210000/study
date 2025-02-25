

N, M, V = map(int, input().split())

graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(0, M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0 for _ in range(N+1)]
visited2 = [0 for _ in range(N+1)]


def DFS(V):
    visited[V] = 1

    print(V, end=' ')
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited[i] == 0:
            DFS(i)

def BFS(V):
    Q = [V]
    visited2[V] = 1

    while Q:
        V = Q.pop(0)

        print(V, end=' ')
        for i in range(1, N + 1):
            if graph[V][i] == 1 and visited2[i] == 0:
                Q.append(i)
                visited2[i] = 1


DFS(V)
print()
BFS(V)

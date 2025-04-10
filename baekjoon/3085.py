import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    tmp = str(sys.stdin.readline().rstrip())
    arr.append(list(tmp))

result = 0

x = [1, -1, 0, 0]
y = [0, 0, 1, -1]

for i in range(0, N):
    for j in range(0, N):
        q = []
        for k in range(4):
            now_x = i + x[k]
            now_y = j + y[k]
            if N > now_x >= 0 and N > now_y >= 0:
                q.append((now_x, now_y))

        while q:
            target = q.pop()
            #print(target)

            arr[i][j], arr[target[0]][target[1]] = arr[target[0]][target[1]], arr[i][j]

            for a1 in range(0, N):
                tmp = ""
                for a2 in range(0, N):
                    tmp += arr[a1][a2]

                before = tmp[0]
                search = 1
                max_search = 1
                for next in range(1, N):
                    if tmp[next] == before:
                        search += 1
                    else:
                        search = 1
                    max_search = max(max_search, search)
                    before = tmp[next]

                max_long = -1
                for c in tmp:
                    max_long = max(max_long, max_search)
                result = max(result, max_long)

            for b1 in range(0, N):
                tmp = ""
                for b2 in range(0, N):
                    tmp += arr[b2][b1]

                before = tmp[0]
                search = 1
                max_search = 1
                for next in range(1, N):
                    if tmp[next] == before:
                        search += 1
                    else:
                        search = 1
                    max_search = max(max_search, search)
                    before = tmp[next]


                max_long = -1
                for c in tmp:
                    max_long = max(max_long, max_search)
                result = max(result, max_long)

            arr[i][j], arr[target[0]][target[1]] = arr[target[0]][target[1]], arr[i][j]

print(result)

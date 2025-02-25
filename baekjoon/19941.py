N, K = map(int, input().split())
s = input()

visited = [0 for i in range(N)]

result = 0

for i in range(0, N):
    if s[i] == 'P':
        for j in range(max(0, i-K), min(i+K+1, N)):
            if s[j] == 'H' and visited[j] == 0:
                result += 1
                visited[j] = 1
                #print(f"{i+1}번째 사람이 {j+1}번째 햄버거 섭취")
                break

print(result)

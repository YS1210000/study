K, N = map(int, input().split())
lan_cable = []
for i in range(K):
    lan_cable.append(int(input()))

A = 0
A += sum(lan_cable)
A //= N

start = 1
end = A

def divide(lan_cable, cut): #가진 케이블 값과 자른 뒤 케이블 크기 -> 나오는 갯수를 돌려줌
    count = 0
    #if cut == 0:
    #    return 1

    for i in lan_cable:
        count += i // cut
    return count


while start <= end:
    mid = (start+end)//2
    if divide(lan_cable, mid) >= N:
        start = mid + 1
        #print(f"now length:{length}, {start}, {end}")
    else:
        end = mid - 1

print(end)

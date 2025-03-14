import sys

T = int(sys.stdin.readline())

for _ in range(T):
    W = sys.stdin.readline().rstrip()
    K = int(sys.stdin.readline())
    dic = {}

    for i in W:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    shortest = 10001
    longest = -1
    while dic:
        key, value = dic.popitem()
        #print(key, value)
        if value >= K:
            idx = []
            for i in range(len(W)):
                if W[i] == key:
                    idx.append(i)
            #print(idx)
            for j in range(len(idx)-K+1):
                shortest = min(shortest, idx[j+K-1] - idx[j])
                longest = max(longest, idx[j+K-1] - idx[j])

    if shortest == 10001 or longest == -1:
        print(-1)
    else:
        print(shortest+1, longest+1)

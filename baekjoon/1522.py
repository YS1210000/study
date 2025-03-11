import sys

st = sys.stdin.readline().rstrip()

count_a = st.count('a')

st += st[0:count_a-1]
#print(st)

start = 0
end = len(st)
result = sys.maxsize

while start <= end - count_a:
    result = min(result, st[start:start+count_a].count('b'))
    #print(st[start:start+count_a])
    start += 1


print(result)

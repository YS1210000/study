import sys
import heapq

n = int(sys.stdin.readline())
q = []
for _ in range(n):
    q.append(list(map(int, sys.stdin.readline().split())))

q.sort(key= lambda x: x[0])

count = 1

meetingroom = [0]

for start, end in q:
    if start >= meetingroom[0]:
        heapq.heappop(meetingroom)
    else:
        count += 1
    heapq.heappush(meetingroom, end)

print(count)

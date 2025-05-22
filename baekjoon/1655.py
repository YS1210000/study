import sys
import heapq

maxheap = [] #작은 값을 - 붙여서 넣음
minheap = [] #큰 값을 넣음

n = int(sys.stdin.readline())

heapq.heappush(maxheap, -int(sys.stdin.readline()))


for i in range(n-1):
    input_num = int(sys.stdin.readline())
    if len(maxheap) > len(minheap):
        tmp = -heapq.heappop(maxheap)
        print(tmp)
        if tmp > input_num:
            heapq.heappush(maxheap, -input_num)
            heapq.heappush(minheap, tmp)
        else:
            heapq.heappush(maxheap, -tmp)
            heapq.heappush(minheap, input_num)

    else:
        tmp = heapq.heappop(minheap)
        tmp2 = heapq.heappop(maxheap)
        print(min(tmp, -tmp2))
        heapq.heappush(maxheap, tmp2)

        if tmp > input_num:
            heapq.heappush(maxheap, -input_num)
            heapq.heappush(minheap, tmp)
        else:
            heapq.heappush(maxheap, -tmp)
            heapq.heappush(minheap, input_num)


if n % 2 == 1:
    print(-heapq.heappop(maxheap))
else:
    print(min(-heapq.heappop(maxheap), heapq.heappop(minheap)))

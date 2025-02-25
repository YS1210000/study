
N, K = map(int,input().split())
arr =[]
result_arr = []

for i in range(2, N+1):
    arr.append(i)

counter = 2
while len(arr):
    for i in arr:
        if i % counter == 0 :
            arr.remove(i)
            result_arr.append(i)
    counter += 1


#print(arr)
#print(result_arr)

print(result_arr[K-1])

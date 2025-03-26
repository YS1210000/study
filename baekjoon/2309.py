import sys

arr = []
for _ in range(9):
    arr.append(int(sys.stdin.readline()))

arr.sort()


for i in range(0, 9):
    for j in range(i, 9):
        if i == j:
            continue
        result = sum(arr) - arr[i] - arr[j]

        if result == 100:
            arr.remove(arr[j])
            arr.remove(arr[i])

            print('\n'.join(map(str, arr)))

            exit(0)

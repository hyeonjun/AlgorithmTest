arr = list(map(int, input().split()))
answer = [i for i in range(1, 6)]
while True:
    for i in range(4):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print(*arr)
    if arr == answer:
        break
def binary(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left+right)//2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    if right >= len(arr):
        return 0
    elif arr[right] == x:
        return 1
    return 0

for _ in range(int(input())):
    n = int(input())
    arr1 = sorted(list(map(int, input().split())))
    m = int(input())
    arr2 = list(map(int, input().split()))
    for i in arr2:
        print(binary(arr1, i))
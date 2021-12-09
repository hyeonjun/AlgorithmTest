def binary(x):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr1[mid] < x:
            left = mid+1
        else:
            right = mid
    if right >= n:
        return 0
    elif arr1[right] == x:
        return 1
    return 0

n = int(input())
arr1 = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))
answer = [binary(i) for i in arr2]
print(*answer)
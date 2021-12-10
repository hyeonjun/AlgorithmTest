def binary():
    left, right = 0, arr[-1]
    while left <= right:
        mid = (left+right)//2
        sumV = sum([mid if i > mid else i for i in arr])
        if sumV <= m:
            left = mid + 1
        else:
            right = mid - 1
    return right

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
print(binary())
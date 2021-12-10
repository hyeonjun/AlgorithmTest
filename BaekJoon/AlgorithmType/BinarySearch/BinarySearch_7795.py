def binary(x):
    left, right = 0, m
    while left < right:
        mid = (left + right) // 2
        if b[mid] < x:
            left = mid+1
        else:
            right = mid
    return left

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    answer = 0
    for i in a:
        answer += binary(i)
    print(answer)
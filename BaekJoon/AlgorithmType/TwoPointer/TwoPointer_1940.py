n = int(input())
m = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0
left, right = 0, n-1
while left < right:
    value = arr[left] + arr[right]
    if value == m:
        answer += 1
        left += 1
        right -= 1
    elif value < m:
        left += 1
    else:
        right -= 1
print(answer)
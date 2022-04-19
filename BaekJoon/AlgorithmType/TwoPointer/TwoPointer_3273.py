n = int(input())
arr = sorted(map(int, input().split()))
x = int(input())
answer = 0
left, right = 0, n-1
while left < right:
    value = arr[left] + arr[right]
    if value == x:
        answer += 1
        left += 1 # right -= 1
    elif value < x:
        left += 1
    else:
        right -= 1
print(answer)
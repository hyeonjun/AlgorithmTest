n = int(input())
nums = sorted(list(map(int, input().split())))
answer = 0

# two_pointer
for i in range(n): # 타겟값: nums[i]
    arr = nums[:i] + nums[i+1:] # 타겟값 제외한 리스트
    left, right = 0, n-2
    while left < right:
        num = arr[left] + arr[right]
        if num == nums[i]:
            answer += 1
            break
        if num < nums[i]:
            left += 1
        else:
            right -= 1
print(answer)
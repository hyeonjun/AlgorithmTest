n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in range(n):
    left, right = 0, len(dp)-1
    while left <= right:
        mid = (left + right) // 2
        if dp[mid] < arr[i]:
            left = mid+1
        else:
            right = mid-1
    if len(dp) <= left:
        dp.append(arr[i])
    else:
        dp[left] = arr[i]
print(len(dp)-1)
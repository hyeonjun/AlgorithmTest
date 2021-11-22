"""
[0, 1, 4, 10, 20, 35, 56, 84, 120, 165, 220]
dp[i] = min(dp[i], dp[i-사면체수])

ex) 5
dp = 1e9 1e9 1e9 1e9 1e9 1e9
i = 1, nums 1 => dp[1] = 1 => dp = 1e9 1 1e9 1e9 1e9 1e9
       nums 4 => break
i = 2, nums 1 => dp[2] = min(dp[2], dp[2-1]+1) => dp = 1e9 1 2 1e9 1e9 1e9
       nums 4 => break
i = 3


"""
import sys
input = sys.stdin.readline
n = int(input())
nums = []
num = 0
idx = 1
while num < n:
    num += (idx * (idx+1)) // 2
    nums.append(num)
    idx += 1
dp = [1e9 for _ in range(n+1)] # dp[x] = 최소 사면체 수, x = 현재 대포알 수
for i in range(1, n+1):
    for j in nums:
        if i == j:
            dp[i] = 1
            break
        if j > i:
            break
        dp[i] = min(dp[i], dp[i-j]+1)
print(dp[n])
"""
2 5 1 1 4
1 2 2 4 6

2 5 1 1
25 1 1
2 5 11
25 11

2 2 1 0 4
1 2 3 2

2 2 1
22 1
2 21

2 2 10
22 10 => i-2

dp[i] = dp[i-1]+dp[i-2] if arr[i]+arr[i-1] < 27 and arr[i] != 0
        dp[i-2] if arr[i] == 0
        dp[i-1] if arr[i]+arr[i-1] > 26
"""
arr = list(input())
n = len(arr)
dp = [0 for _ in range(n+1)]
dp[0:2] = [1, 1]
mod = 1000000
if arr[0] == '0':
    print(0)
else:
    # 성공
    for i in range(2, n+1):
        if int(arr[i-1]) > 0:
            dp[i] = dp[i-1]
        num = int(arr[i - 2] + arr[i - 1])
        if 10 <= num <= 26:
            dp[i] += dp[i-2]
    print(dp[n] % mod)
    # 실패
    # for i in range(2, n + 1):
    #     num = int(arr[i - 2] + arr[i - 1])
    #     if arr[i - 1] == '0':
    #         dp[i] = dp[i - 2] % mod
    #     elif num > 26:
    #         dp[i] = dp[i - 1] % mod
    #     elif num < 27:
    #         dp[i] = (dp[i - 1] + dp[i - 2]) % mod
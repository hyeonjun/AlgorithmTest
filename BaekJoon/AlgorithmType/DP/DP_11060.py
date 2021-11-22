"""
10
1 2 0 1 3 2 1 5 4 2
"""
n = int(input())
arr = list(map(int, input().split()))
dp = [1e9 for _ in range(n)]
dp[0] = 0 # 출발 위치
for i in range(n):
    for j in range(1,arr[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1)
print(dp[n-1] if dp[n-1] != 1e9 else -1)
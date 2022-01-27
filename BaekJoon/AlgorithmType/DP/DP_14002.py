n = int(input())
arr = list(map(int, input().split()))
dp = [[arr[i]] for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            if len(dp[i]) < len(dp[j])+1:
                dp[i] = dp[j] + [arr[i]]
dp.sort(key=lambda x:-len(x))
print(len(dp[0]))
print(*dp[0])
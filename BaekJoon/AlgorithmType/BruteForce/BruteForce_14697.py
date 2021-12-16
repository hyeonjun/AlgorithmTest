a, b, c, n = map(int, input().split())

# BruteForce
flag = False
for i in range(n//a+1):
    for j in range((n-(a*i))//b+1):
        for k in range((n-(a*i+b*j))//c+1):
            if a*i + b*j + c*k == n:
                flag = True
                break
print(1 if flag else 0)

# DP
dp = [0 for _ in range(301)]
dp[a] = dp[b] = dp[c] = 1
for i in range(a, n+1):
    for j in [a, b, c]:
        if i >= j and dp[i-j]:
            dp[i] = 1
print(dp[n])

n = int(input())
seq = list(map(int, input().split()))
dp = [1, 1]
answer = 1
for i in range(1, n):
    if seq[i-1] <= seq[i]:
        dp[0] += 1
        answer = max(answer, dp[0])
    else:
        dp[0] = 1
    if seq[i-1] >= seq[i]:
        dp[1] += 1
        answer = max(answer, dp[1])
    else:
        dp[1] = 1
print(answer)
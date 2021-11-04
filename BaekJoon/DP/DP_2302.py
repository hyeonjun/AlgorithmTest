"""
vip석으로 인해 나눠진 남은 좌석들에 대해 각각 배치할 수 있는 경우의 수

1 -> 1
2 -> 12 21
3 -> 123 132 213
4 -> 1234 2134 2143 1324 1243
5 -> 12345 12354 12435 21345 21354 21435 13245 13254
...

즉, dp[i] = dp[i-1]+dp[i-2]
"""

n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]
dp = [1,1,2]
for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2])
answer = 1
if m > 0:
    idx = 0
    for v in vip:
        answer *= dp[v-1-idx]
        idx = v
    answer *= dp[n-idx]
else:
    answer = dp[n]
print(answer)
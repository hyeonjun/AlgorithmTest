"""
최소의 돈을 지불 -> 카드 N개 구입
카드 i개 -> Pi
dp[n], 카드 개수 n
P => 1 5 6 7
n => 1      2           3           4
    p[1]   p[1]+dp[1]  dp[2]+p[1]   dp[3]+p[1]
           p[2]        dp[1]+p[2]   dp[2]+p[2]
                       p[3]         dp[1]+p[3]
                                    p[4]

i >= 2, 1 <= j <= i
dp[i] =
   min(dp[i], dp[i-1]+p[1], dp[i-2]+p[2]... dp[1]+p[j])
"""
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [1e9 for _ in range(n+1)]
dp[0] = 0
for i in range(n+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j]+p[j])
print(dp[n])
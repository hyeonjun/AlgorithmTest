"""
dp[n], 카드 개수 n
P => 1 5 6 7
n => 1    2           3             4
    p[1]  dp[1]+p[1]  dp[2]+p[1]    dp[3]+p[1]
          p[2]        dp[1]+p[2]    dp[2]+p[2]
                      p[3]          dp[1]+p[3]
                                    p[4]

"""
n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = p[1]

for i in range(2, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+p[j])

print(dp[n])

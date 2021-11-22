"""
n번째 직사각형 채우기 = (2*1 세로 + n-1번째 직사각형)의 경우의 수 +
                (2*1 가로 + n-2번째 직사각형)의 경우의 수 + (2*2 + n-2번째 직가각형)의 경우의 수

 => dp[i] = dp[i-1] + dp[i-2] * 2
"""

dp = [0 for _ in range(251)]
dp[0:3] = [1, 1, 3]
for i in range(3, 251):
    dp[i] = dp[i-1] + dp[i-2] * 2
while True:
    try:
        n = int(input())
        print(dp[n])
    except:
        break
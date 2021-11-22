"""
SK, CK
1 -> 1 CK
2 -> 1 1 SK
3 -> 1 1 / 1 -> CK
4 -> 3 1 -> SK

5 -> 1, 3, 4 경우의 수
1 -> 4 경우 -> CK
3 -> 2 경우 -> CK
4 -> 1 경우 -> SK
"""
n = int(input())
dp = ["", "CY", "SK", "CY", "SK"]
for i in range(5, n+1):
    win = "SK" if "CY" in [dp[i-1], dp[i-3], dp[i-4]] else "CY"
    dp.append(win)
print(dp[n])
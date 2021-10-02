# 방법 1
def dp(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return dp(n-1) + dp(n-2) + dp(n-3)

for _ in range(int(input())):
    n = int(input())
    print(dp(n))

# 방법 2
for _ in range(int(input())):
    n = int(input())
    dp = [1, 2, 4]
    if n == 1:
        print(dp[0])
    elif n == 2:
        print(dp[1])
    elif n == 3:
        print(dp[2])
    else:
        for i in range(3, n):
            dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])
        print(dp[n - 1])


"""
1 -> 1 => 1
2 -> 1+1, 2 => 2
3 -> 1+1+1, 1+2, 2+1, 3 => 4
4 -> 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 3+1, 1+3, 2+2 => 7
5 -> 1+1+1+1+1, 2+1+1+1, 1+2+1+1, 1+1+2+1, 1+1+1+2, 2+2+1, 1+2+2, 2+1+2, 1+1+3, 1+3+1, 3+1+1, 2+3, 3+2 => 13

1, 2, 4, 7, 13
7 => 1 + 2 + 4
13 => 2+ 4+ 7
n > 3: f(n) = f(n-1) + f(n-2) + f(n-3)
"""
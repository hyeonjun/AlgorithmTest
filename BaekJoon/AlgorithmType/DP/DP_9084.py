"""
dp 1  2    3       4         5           6       7  8  9  10  11  12  13  14  15  16  17  18  19  20
c
1 1 1+1 1+1+1  1+1+1+1  1+1+1+1+1  1+1+1+1+1+1  ...
2 0  2   1+2    1+1+2    1+1+1+2
                 2+2      1+2+2

"""


for _ in range(int(input())):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _  in range(m+1)]
    dp[0] = 1
    for c in coin:
        for i in range(1, m+1):
            if i-c >= 0:
                dp[i] += dp[i-c]
    print(dp[m])
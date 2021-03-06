# 제곱수의 합
"""
0 - 0
1 - 1^2 -------------------- 1
2 - 1^2 + 1^2
3 - 1^2 + 1^2 + 1^2
4 - 2^2 -------------------- 1
5 - 1^2 + 2^2
6 - 1^2 + 1^2 + 2^2
7 - 1^2 + 1^2 + 1^2 + 2^2
8 - 2^2 + 2^2 -------------- 2
9 - 3^2 -------------------- 1
10 - 3^2 + 1^2
11 - 3^2 + 1^2 + 1^2
12 - 2^2 + 2^2 + 2^2
13 - 3^2 + 2^2
14 - 3^2 + 2^2 + 1^1
15 - 3^2 + 2^2 + 1^1 + 1^1
16 - 4^2 -------------------- 1
"""
n = int(input())
dp = [0 for _ in range(n+1)]
square = [i*i for i in range(1, int(n**0.5)+1)]
for i in range(1, n+1):
    tmp = []
    for j in square:
        if j > i:
            break
        tmp.append(dp[i-j])
    dp[i] = min(tmp)+1
print(dp[n])

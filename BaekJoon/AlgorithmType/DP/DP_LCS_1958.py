"""
* Longest Common Subsequence
    - Longest Common Subsequence : 문자열이 연속되지 않아도 공통되는 문자열들 중 가장 긴 것
    - Longest Common Substring : 문자열이 연속으로 공통되는 문자열들 중 가장 긴 것
"""
string = [input() for _ in range(3)]
a, b, c = len(string[0]), len(string[1]), len(string[2])
dp = [[[0 for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            if string[0][i-1] == string[1][j-1] == string[2][k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                # 이전에 공통되는 문자열들 중 가장 긴 것을 가져온다
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
print(dp[a][b][c])
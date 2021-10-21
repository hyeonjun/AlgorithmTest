import sys
input = sys.stdin.readline
n = int(input())
size = [list(map(int,input().split())) for _ in range(n)]
dp = [[sys.maxsize for _ in range(n)] for _ in range(n)]
# dp[i][j] = i~j 행렬의 곱 연산 횟수 최솟값

for i in range(n): # 같은 행렬 곱 x
    dp[i][i] = 0

for i in range(1, n):
    for start in range(n):
        end = start+i
        if end >= n:
            break
        for fixed in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][fixed] + dp[fixed+1][end] + (size[start][0] * size[fixed+1][0] * size[end][1]))
        """
        a, b, c, d 행렬
        dp(a) + dp(b, c, d) + 비용
        dp(a, b) + dp(c, d) + 비용
        dp(a, b, c) + dp(d) + 비용
        """
print(dp[0][-1])




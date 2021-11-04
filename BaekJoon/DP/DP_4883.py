"""
dp[출발][도착] = 비용

    1   2   3
1       7
2
3
4

첫 행
 => dp[1][0] = dp[0][1]
    dp[1][1] = dp[0][1], dp[1][0], dp[0][1]+dp[0][2]
    dp[1][2] = dp[0][1], dp[1][1], dp[0][1]+dp[0][2]
"""
tc = 0
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int,input().split())) for _ in range(n)]
    tc += 1

    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[1][0] = graph[1][0] + graph[0][1]
    dp[1][1] = graph[1][1] + min(dp[1][0], graph[0][1], graph[0][1]+graph[0][2])
    dp[1][2] = graph[1][2] + min(dp[1][1], graph[0][1], graph[0][1]+graph[0][2])

    for i in range(2, n):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + graph[i][j]
            elif j == 1:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + graph[i][j]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + graph[i][j]
    print(f'{tc}. {dp[-1][1]}')

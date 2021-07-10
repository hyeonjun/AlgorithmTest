def solution(arr):
    opCount = len(arr) // 2 + 1
    max_dp = [[-float('inf') for _ in range(opCount)] for _ in range(opCount)]
    min_dp = [[float('inf') for _ in range(opCount)] for _ in range(opCount)]

    for i in range(opCount):
        max_dp[i][i] = int(arr[i * 2])
        min_dp[i][i] = int(arr[i * 2])
    for cnt in range(1, opCount):
        for i in range(opCount - cnt):
            j = i + cnt
            for k in range(i, j):
                if arr[k * 2 + 1] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])
    return max_dp[0][opCount - 1]

print(solution(["1", "-", "3", "+", "5", "-", "8"])) # 1
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])) # 3
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        r, c = len(matrix), len(matrix[0])
        def dfs(x, y):
            if dp[x][y] != -1:
                return dp[x][y]
            dp[x][y] = 1
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] > matrix[x][y]:
                    if dp[nx][ny] == -1:
                        dfs(nx, ny)
                    dp[x][y] = max(dp[x][y], dp[nx][ny]+1)
        answer = 0
        dp = [[-1 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if dp[i][j] == -1:
                    dfs(i, j)
                    answer = max(answer, dp[i][j])
        return answer
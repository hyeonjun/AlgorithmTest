from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0

        obstacleGrid[0][0] = 1
        for i in range(1, m):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1)
        for i in range(1, n):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)

        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:  # 장애물 있음
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            if obstacleGrid[0][i] == 1: break
            dp[0][i] = 1
        for i in range(n):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return ((n+1) * (n+2) * (n+3) * (n+4)) // 24 # (n+4)C4


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[i for i in range(5, 0, -1)] for _ in range(n)]

        """
              a   e   i   o   u
        n=1   5   4   3   2   1
        n=2  15  10   6   3   1
        n=3  35  20  10   4   1

        dp[i][j] = dp[i-1][j] + dp[i][j+1]
        """

        for i in range(1, n):
            for j in range(3, -1, -1):
                dp[i][j] = dp[i - 1][j] + dp[i][j + 1]
        return dp[n - 1][0]
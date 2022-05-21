from typing import List

# Bottom-Up DP 1, 2020ms
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9 for _ in range(amount+1)]
        dp[0] = 0
        for c in coins:
            for i in range(c, amount+1):
                if i-c < 0:
                    break
                dp[i] = min(dp[i], dp[i-c] + 1)
        return -1 if dp[-1] == 1e9 else dp[-1]

# Bottom-Up DP 2, 1754ms
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [1e9 for _ in range(amount+1)]
        coins.sort()
        for c in coins:
            if c <= amount: dp[c] = 1
        for i in range(1, amount):
            for c in coins:
                if i + c <= amount:
                    dp[i+c] = min(dp[i+c], dp[i]+1)
        return -1 if dp[-1] == 1e9 else dp[-1]

# BFS + Memoization(DP), 830ms
from collections import deque
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = [0 for _ in range(amount+1)]
        queue = deque([amount])
        while queue:
            x = queue.popleft()
            if x == 0:
                return dp[x]
            for c in coins:
                nx = x - c
                if 0 <= nx and not dp[nx]:
                    queue.append(nx)
                    dp[nx] = dp[x]+1
        return -1

# Bitmask, 70ms -> 뭘까 이건
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        answer, prev = 0, 1 << amount

        while prev & 1 == 0:
            cur = prev
            for c in coins:
                cur |= prev >> c
            if cur == prev: return -1
            answer += 1
            prev = cur
        return answer
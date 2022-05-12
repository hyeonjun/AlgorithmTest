from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []

        def dfs(cnt, result):
            if len(result) == n:
                answer.append(result[:])
                return

            for x, y in cnt.items():
                if y > 0:
                    result.append(x)
                    cnt[x] -= 1
                    dfs(cnt, result)
                    cnt[x] += 1
                    result.pop()

        dfs(Counter(nums), [])
        return answer


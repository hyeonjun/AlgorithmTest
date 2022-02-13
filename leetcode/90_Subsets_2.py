class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        def dfs(idx, num):
            if len(num) == k:
                answer.add(tuple(num[:]))
                return

            cur = None
            for i in range(idx, n):
                if not visited[i] and nums[i] != cur:
                    cur = nums[i]
                    num.append(nums[i])
                    visited[i] = True
                    dfs(i+1, num)
                    visited[i] = False
                    num.pop()

        answer = set()
        n = len(nums)
        visited = [False for _ in range(n)]
        for k in range(n+1):
            dfs(0, [])
        return answer

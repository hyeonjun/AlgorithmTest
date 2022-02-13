# Cascading
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = [[]]
        for n in nums:
            answer += [a+[n] for a in answer]
        return answer

# BackTracking
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = []
        def dfs(idx, num):
            if k == len(num):
                answer.append(num[:])
                return

            for i in range(idx, n):
                num.append(nums[i])
                dfs(i+1, num)
                num.pop()

        n = len(nums)
        for k in range(n+1):
            dfs(0, [])
        return answer

# Bit-Mask
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        answer = []
        for i in range(1 << n):
            answer.append([nums[j] for j in range(n) if i & (1 << j)])
        return answer

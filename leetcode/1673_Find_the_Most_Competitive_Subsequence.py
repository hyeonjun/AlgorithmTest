# Stack
class Solution:
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        stack = []
        nk = len(nums) - k
        for n in nums:
            while nk > 0 and stack and stack[-1] > n:
                stack.pop()
                nk -= 1
            stack.append(n)
        stack = stack[:k]
        return stack

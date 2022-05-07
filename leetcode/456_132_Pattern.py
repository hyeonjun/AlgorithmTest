from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, s = [], -1e11
        for n in reversed(nums):
            if n < s:
                return True
            while stack and stack[-1] < n:
                s = stack.pop()
            stack.append(n)
        return False
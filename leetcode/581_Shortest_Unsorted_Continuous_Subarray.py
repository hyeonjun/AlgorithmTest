from typing import List

# Solution 1 - Sort, 349ms
class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        start, end = len(nums), 0
        for i in range(len(nums)):
            if sort_nums[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end - start + 1 > 0 else 0

# Solution 2 - Stack, 448ms
class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums), 0

        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)

        return end - start + 1 if end - start > 0 else 0


# Solution 3, 218ms
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        start, end = 0, n - 1
        while start < len(nums) - 1 and nums[start] <= nums[start + 1]:
            start += 1
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1

        if start > end:
            return 0

        minV, maxV = min(nums[start:end + 1]), max(nums[start:end + 1])
        while start > 0 and minV < nums[start - 1]:
            start -= 1
        while end < len(nums) - 1 and nums[end + 1] < maxV:
            end += 1
        return end - start + 1
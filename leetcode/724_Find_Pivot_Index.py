class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        ps = [0]
        for i in range(1, len(nums) + 1):
            ps.append(ps[-1] + nums[i - 1])

        for i in range(len(ps) - 1):
            if ps[i] == ps[-1] - ps[i + 1]:
                return i
        return -1

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        total = sum(nums)
        left = 0
        for i in range(n):
            right = total - nums[i] - left
            if left == right:
                return i
            left += nums[i]
        return -1
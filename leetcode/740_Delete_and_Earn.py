class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxV = max(nums)
        points = [0 for _ in range(maxV + 1)]
        prev, cur = 0, 0
        for num in nums:
            points[num] += num

        for p in points:
            prev, cur = cur, max(prev + p, cur)
        return cur

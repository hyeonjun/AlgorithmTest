class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        answer = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
            answer += dp[i]
        return answer

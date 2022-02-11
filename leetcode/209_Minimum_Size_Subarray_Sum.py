# Two Pointer, Prefix Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        sumV = 0
        answer = n+1
        left = 0
        for right in range(n):
            sumV += nums[right]
            while target <= sumV:
                answer = min(answer, right - left+1)
                sumV -= nums[left]
                left += 1
        return answer if answer != n+1 else 0

solution = Solution()
print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))

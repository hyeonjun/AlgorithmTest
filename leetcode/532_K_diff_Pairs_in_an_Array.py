class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        from collections import Counter
        answer = 0
        cnt = Counter(nums)
        for n in cnt:
            if k > 0 and n-k in cnt or k == 0 and cnt[n] > 1:
                answer += 1
        return answer


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums.sort()
        answer = 0
        left = 0

        for right in range(1, len(nums)):
            if right + 1 < len(nums) and nums[right] == nums[right + 1]:
                continue

            while 0 < left and nums[left] == nums[left - 1]:
                left += 1

            while k < nums[right] - nums[left] and left + 1 < right:
                left += 1
            if nums[right] - nums[left] == k:
                answer += 1

        return answer
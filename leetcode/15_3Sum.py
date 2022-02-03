class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = set()
        for i in range(len(nums)):
            left, right = i+1, len(nums)-1
            while left < right:
                sumV = nums[i] + nums[left] + nums[right]
                if sumV < 0:
                    left += 1
                elif sumV == 0:
                    answer.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                else:
                    right-=1
        return answer
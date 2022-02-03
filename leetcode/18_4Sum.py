# Sort, Two Pointer
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        answer = set()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    sumV = nums[i] + nums[j] + nums[left] + nums[right]
                    if sumV < target:
                        left += 1
                    elif sumV == target:
                        answer.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    else:
                        right -= 1
        return answer
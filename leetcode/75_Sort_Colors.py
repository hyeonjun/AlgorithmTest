class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # nums.sort()

        p, left, right = 0, 0, len(nums)-1
        while p <= right:
            if nums[p] < 1:
                nums[p], nums[left] = nums[left], nums[p]
                p += 1
                left += 1
            elif nums[p] > 1:
                nums[p], nums[right] = nums[right], nums[p]
                right -= 1
            else:
                p += 1

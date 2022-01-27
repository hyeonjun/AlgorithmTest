class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            if nums[i] != val:
               nums[cnt] = nums[i]
               cnt += 1
        return cnt

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right-1]
                right -= 1
            else:
                left += 1
        return right

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)

        for i in range(nums.count(val)):
                nums.remove(val)
                n -= 1

        return n
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt = 1
        for i in range(1, len(nums)):
            if nums[cnt-1] != nums[i]:
                nums[cnt] = nums[i]
                cnt += 1
        print(nums)
        return cnt
s = Solution()
s.removeDuplicates([1, 1, 2])
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
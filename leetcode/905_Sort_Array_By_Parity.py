from typing import List


class Solution1:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lambda x:x%2)


class Solution2:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd, even = [], [] # 홀수, 짝수
        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        return even + odd

class Solution3:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] % 2 and not nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i]
            if not nums[i] % 2:
                i += 1
            if nums[j] % 2:
                j -= 1
        return nums
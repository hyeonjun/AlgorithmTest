from typing import List
from collections import Counter


# Solution 1 - Two Pointer, 908ms
class Solution1:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        answer = 0
        while left < right:
            val = nums[left] + nums[right]
            if val == k:
                left += 1
                right -= 1
                answer += 1
            elif val > k:
                right -= 1
            else:
                left += 1
        return answer


# Solution 2 - HashMap, 634ms
class Solution2:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        answer = 0
        for c in count:
            r = k - c
            if c < r:
                answer += min(count[c], count[r])
            elif c == r:
                answer += count[c] //2
        return answer
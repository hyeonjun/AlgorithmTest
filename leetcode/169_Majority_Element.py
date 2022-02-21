class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        from collections import Counter
        return Counter(nums).most_common(1)[0][0]

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        answer = nums[0]
        cnt = 1
        for i in nums[1:]:
            if i == answer:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    answer = i
                    cnt = 1
        return answer

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort() # sort() time < sorted() time
        return nums[len(nums)//2]

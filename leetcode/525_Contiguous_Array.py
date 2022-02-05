# Brute Force - Time Limit Exceeded
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            zero, one = 0, 0
            for j in range(len(nums)):
                if nums[j] == 0:
                    zero += 1
                else:
                    one += 1
                if zero == one:
                    answer = max(answer , i-j+1)
        return answer

# Hash Table, Prefix Sum
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        count = 0
        answer = 0
        hashmap = {0: 0}
        for i in range(1, len(nums)+1):
            count += 1 if nums[i-1] else -1
            if count in hashmap:
                answer = max(answer, i - hashmap[count])
            else:
                hashmap[count] = i
        return answer
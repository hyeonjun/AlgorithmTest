# Time Limit Exceeded
class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                answer = max(answer, nums[i] ^ nums[j])
        return answer

solution = Solution()
print(solution.findMaximumXOR([3,10,5,25,2,8]))

# 전혀 이해 안됨
class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        answer = 0
        for i in reversed(range(32)):
            prefixes = set([x >> i for x in nums])
            answer <<= 1
            candidate = answer + 1
            for p in prefixes:
                if candidate ^ p in prefixes:
                    answer = candidate
                    break      
        return answer

solution = Solution()
print(solution.findMaximumXOR([3,10,5,25,2,8]))
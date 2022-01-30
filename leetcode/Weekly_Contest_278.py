# LeetCode - Weekly Contest 278
# 2022.01.30
# 11:30 - 13:00

# 1번
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        while True:
            idx = self.binary(nums, left, right, original)
            if idx is None:
                break
            original *= 2
            left = idx + 1

        return original

    def binary(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return None

# 2번
class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        answer = [0]
        one = nums.count(1)
        zero = 0
        score = one+zero
        for i in range(1, len(nums)+1):
            if nums[i-1] == 0:
                zero += 1
            else:
                one -= 1
            if score < one+zero:
                score = one+zero
                answer.clear()
            if score == one+zero:
                answer.append(i)
        return answer

# 3번
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)

        powerValue = [1 for _ in range(k+1)]
        for i in range(1, k+1):
            powerValue[i] = powerValue[i - 1] * power % modulo

        sOrd = [ord(ch) - ord('a') + 1 for ch in s]

        result = sum([sOrd[n-k+i] * powerValue[i] for i in range(k)])
        idx = n-k
        for i in range(n-k-1, -1, -1):
            result = (result * power + sOrd[i] - sOrd[i+k] * powerValue[k]) % modulo
            if result == hashValue:
                idx = i
        return s[idx:idx+k]
# solution = Solution()
# print(solution.subStrHash("leetcode", 7, 20 ,2, 0))

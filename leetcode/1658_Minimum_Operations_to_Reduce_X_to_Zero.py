class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sumV = sum(nums) # 11 = sum([1, 1, 4, 2, 3])
        if sumV < x:
            return -1
        if sumV == x:
            return len(nums)

        target = sumV - x # 6 = 11 - 5
        answer = 0
        left = 0
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while target < total:
                total -= nums[left]
                left += 1
            if total == target:
                answer = max(answer, right - left + 1)
        return len(nums)-answer if answer else -1

"""
EX1)
nums = [1, 1, 4, 2, 3], x = 5
target = 11 - 5 = 6

total = 0
left, right = 0, 0
total = sum([1])

left, right = 0, 1
total = sum([1, 1])

left, right = 0, 2
total = sum([1, 1, 4])
total == target -> answer = 3
return len(nums)-answer = 5-3 = 2

EX2)
nums = [3, 2, 20, 1, 1, 3], x = 10
target = 30 - 10 = 20

total = 0
left, right = 0, 0
total = sum([3]) = 3
total != target

left, right = 0, 1
total = sum([3, 2]) = 5
total != target

left, right = 0, 2
total = sum([3, 2, 20]) = 25
target < total
  -> total - nums[left] = 25 - 3
    -> left += 1 => left = 1
  -> total - nums[left] = 22 - 2
    -> left += 1 => left = 2
    -> total == target
      -> answer = max(answer = 0, right - left + 1 = 1) = 1

left, right = 2, 3
total = sum([20, 1]) = 21
target < total
  -> total - nums[left] = 21 - 1
    -> left += 1 => left = 3
    -> total == target
      -> answer = max(answer = 1, right - left + 1 = 1) = 1

left, right = 3, 4
total = sum([20, 1]) = 21
target < total
  -> total - nums[left] = 21 - 1
    -> left += 1 => left = 4
    -> total == target
      -> answer = max(answer = 1, right - left + 1 = 1) = 1

left, right = 4, 5
total = sum([20, 3]) = 23
target < total
  -> total - nums[left] = 23 - 1
    -> left += 1 => left = 5
  -> total - nums[left] = 22 - 3

return len(nums) - answer = 5
"""

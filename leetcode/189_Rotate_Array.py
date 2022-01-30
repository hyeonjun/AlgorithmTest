from collections import deque
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        dq = deque(nums)
        k %= len(nums)
        for _ in range(k):
            dq.appendleft(dq.pop())
        nums[:] = list(dq)


from collections import deque
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        dq = deque(nums)
        k %= len(nums)
        dq.rotate(k)
        nums[:] = list(dq)
        return nums

# reverse n-k
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        end = n - 1

        self.reverse(nums, 0, end - k)  # 4 3 2 1 5 6 7
        self.reverse(nums, end - k + 1, end)  # 4 3 2 1 7 6 5
        self.reverse(nums, 0, end)  # 5 6 7 4 3 2 1

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
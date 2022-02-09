class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    answer += 1
        return answer

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        for n in nums:
                hashmap[n] += 1
        return sum(hashmap[n] * hashmap[n-k] for n in hashmap if n-k in hashmap)

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from collections import Counter
        cnt = Counter(nums)
        return sum(cnt[n] * cnt[n-k] for n in cnt if n-k in cnt)
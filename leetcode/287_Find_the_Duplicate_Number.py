class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums).most_common(1)
        return cnt[0][0]

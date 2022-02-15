class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        # most_common(n): n개의 빈도수 높은 순으로 받음
        cnt = Counter(nums).most_common()
        return cnt[-1][0]

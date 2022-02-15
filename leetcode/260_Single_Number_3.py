class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter(nums).most_common()
        return [cnt[-1][0], cnt[-2][0]]

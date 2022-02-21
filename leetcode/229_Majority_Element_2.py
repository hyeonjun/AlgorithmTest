class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        from collections import Counter
        appear = len(nums) // 3
        answer = []
        cnt = Counter(nums)
        for i in cnt:
            if cnt[i] > appear:
                answer.append(i)
        return answer

# Hash Map
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        n = len(nums1)

        for i in range(n):
            for j in range(n):
                hashmap[nums1[i] + nums2[j]] += 1

        answer = 0
        for k in range(n):
            for l in range(n):
                x = 0 - nums3[k] - nums4[l]
                if x in hashmap:
                    answer += hashmap[x]
        return answer
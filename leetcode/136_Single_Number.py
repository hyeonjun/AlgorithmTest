class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for d in dic:
            if dic[d] == 1:
                return d
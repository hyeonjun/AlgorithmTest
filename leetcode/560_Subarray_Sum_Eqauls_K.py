# Time Limit Exceeded
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        ps = [0]
        for i in range(1, len(nums)+1):
            ps.append(ps[-1] + nums[i-1])
        answer = 0
        for i in range(1, len(ps)):
            for j in range(i):
                if ps[i] - ps[j] == k:
                    answer += 1
        return answer

# Prefix Sum
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        answer = 0
        sumV = 0
        dic = defaultdict(int)
        dic[0] = 1
        for i in range(len(nums)):
            sumV += nums[i]
            answer += dic[sumV-k] # 현재 구간합에서 k만큼 뺀 값이 있으면 그 값을 빼면 k이므로
            dic[sumV] += 1
        return answer

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        answer = 0
        sumV = 0
        dic = {0: 1}
        for i in range(len(nums)):
            sumV += nums[i]
            answer += dic.get(sumV-k, 0)
            dic[sumV] = dic.get(sumV, 0) + 1
        return answer
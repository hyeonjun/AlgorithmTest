# 1349ms
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        answer = 0
        left, right = 0, 1
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                answer = max(answer, profit)
            else:
                left = right
            right += 1
        return answer

# 956ms
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        answer = 0
        maxV, minV = -1, prices[0]
        for p in prices:
            if minV > p:
                answer = max(answer, maxV - minV)
                maxV, minV = -1, p
            elif maxV < p:
                maxV = p
        return max(answer, maxV - minV)
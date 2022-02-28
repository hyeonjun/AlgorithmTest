class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        answer = []
        for n in nums:
            if answer and answer[-1][1] == n-1:
                answer[-1][1] = n
            else:
                answer.append([n, n])
        return [str(i)+"->"+str(j) if i != j else str(i) for i, j in answer]
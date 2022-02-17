class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []

        def dfs(idx, sumV, arr):
            if sumV == target:
                answer.append(arr[:])
                return
            if sumV > target:
                return
            for i in range(idx, len(candidates)):
                sumV += candidates[i]
                arr.append(candidates[i])
                dfs(i, sumV, arr)
                arr.pop()
                sumV -= candidates[i]

        dfs(0, 0, [])

        return answer

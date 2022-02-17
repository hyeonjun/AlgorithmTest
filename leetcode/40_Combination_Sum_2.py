class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        answer = []

        def dfs(idx, sumV, arr):
            if sumV == target:
                answer.append(arr[:])
                return
            if sumV > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                sumV += candidates[i]
                arr.append(candidates[i])
                dfs(i+1, sumV, arr)
                arr.pop()
                sumV -= candidates[i]

        dfs(0, 0, [])
        return answer

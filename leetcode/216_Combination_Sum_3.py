class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        answer = []
        def dfs(idx, depth, sumV, arr):
            if depth == k:
                if sumV == n:
                    answer.append(arr[:])
                    return
            if sumV > n:
                return

            for i in range(idx, 10):
                sumV += i
                arr.append(i)
                dfs(i+1, depth+1, sumV, arr)
                arr.pop()
                sumV -= i
        dfs(1, 0, 0, [])
        return answer

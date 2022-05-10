from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2str = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        n = len(digits)
        answer = []
        def dfs(idx, res):
            if idx == n:
                if len(res) > 0:
                    answer.append(''.join(res))
                return
            for s in num2str[digits[idx]]:
                res.append(s)
                dfs(idx+1, res)
                res.pop()
        dfs(0, [])
        return list(answer)
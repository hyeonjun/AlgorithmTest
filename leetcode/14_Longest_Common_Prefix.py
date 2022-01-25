# 24ms
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ''
        for i in range(len(strs[0])):
            w = strs[0][i]
            for word in strs:
                if len(word) <= i or word[i] != w:
                    return answer
            answer += w
        return answer

# 50ms
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ''
        strs.sort() # 공통 접두사만 알면 되기 때문에 정렬 시킨 후
        for x, y in zip(strs[0], strs[-1]): # 문자열 리스트의 첫 번째 요소와 마지막 요소만 확인하면 된다.
            if x == y:
                answer += x
            else:
                break
        return answer
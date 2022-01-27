class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        answer = -1
        n, m = len(haystack), len(needle)
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                answer = i
                break
        return answer

solution = Solution()
print(solution.strStr("hello", "ll"))

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        def getPi(n):
            j = 0
            pi = [0 for _ in range(n)]
            for i in range(1, n):
                while j > 0 and needle[i] != needle[j]:
                    j = pi[j-1]
                if needle[i] == needle[j]:
                    j += 1
                    pi[i] = j
            return pi

        def KMP():
            pi = getPi(len(needle))
            j = 0
            for i in range(len(haystack)):
                while j > 0 and haystack[i] != needle[j]:
                    j = pi[j-1]
                if haystack[i] == needle[j]:
                    if j == len(needle) - 1:
                        return i-len(needle)+1
                    else:
                        j += 1
            return -1

        return KMP()

solution = Solution()
print(solution.strStr("abcdefghi", "def"))


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)
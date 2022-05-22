class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = 0

        def palindrom(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        for i in range(len(s)):
            answer += palindrom(i, i)  # "aba" -> i = j = 1
            answer += palindrom(i, i + 1)  # "abba" -> i =1, j =2
        return answer
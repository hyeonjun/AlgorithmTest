class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        check = 0
        for i in range(len(s)):
            for j in range(idx, len(t)):
                if s[i] == t[j]:
                    idx = j+1
                    check += 1
                    break
        return check == len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

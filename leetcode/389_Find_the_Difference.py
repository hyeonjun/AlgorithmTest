class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in t:
            if i in dic:
                dic[i] -= 1
            else:
                return i
            if dic[i] < 0:
                return i

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in set(t):
            if s.count(i) != t.count(i):
                return i
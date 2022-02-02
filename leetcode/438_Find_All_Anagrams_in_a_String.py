# Hash Table, Sliding Window
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import defaultdict
        n, m = len(s), len(p)
        if n < m:
            return []

        countP = defaultdict(int)
        for i in p:
            countP[i] += 1

        countS = defaultdict(int)
        for i in range(m):
            countS[s[i]] += 1
        answer = []
        if countS == countP:
            answer.append(0)

        for i in range(1, n - m + 1):
            x = s[i - 1]
            countS[x] -= 1
            if countS[x] == 0:
                del countS[x]
            y = s[i + m - 1]
            countS[y] += 1
            if countP == countS:
                answer.append(i)
        return answer

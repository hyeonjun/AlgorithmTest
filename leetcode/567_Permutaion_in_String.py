class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict
        n, m = len(s1), len(s2)
        if n > m:
            return False

        count1 = defaultdict(int)
        for s in s1:
            count1[s] += 1

        count2 = defaultdict(int)
        for i in range(n):
            count2[s2[i]] += 1
        if count1 == count2:
            return True

        for i in range(1, m - n + 1):
            x = s2[i - 1]
            count2[x] -= 1
            if count2[x] == 0:
                del count2[x]

            y = s2[i + n - 1]
            count2[y] += 1

            if count1 == count2:
                return True
        return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        count1, count2 = [0] * 26, [0] * 26
        for i in range(n):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(1, m-n+1):
            count2[ord(s2[i-1]) - ord('a')] -= 1
            count2[ord(s2[i+n-1]) - ord('a')] += 1
            if count1 == count2:
                return True
        return False
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s = str(n)
        l = len(s)
        answer = 0
        for i in range(len(s)):
            if i == 0 or s[i] >= s[i-1]:
                answer += int(s[i]) * (10 ** (l-1))
            else:
                return self.monotoneIncreasingDigits(answer-1)
            l -= 1
        return answer

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n < 10:
            return n
        s = str(n)

        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                break
         # i가 len(s)-2이면 위 for loop에서 끝까지 갔다는 얘기고,
         # 마지막으로 확인했을 때 맞으면 return
        if i == len(s)-2 and s[i] <= s[i+1]:
            return n
        # 1200 -> i = 1
        while i > 0 and s[i] == s[i-1]:
            print(i, s[i], s[i-1])
            i -= 1
        # answer = 1200 -> 11 -> 1199
        answer = (s[:i] + str(int(s[i]) - 1)).ljust(len(s), '9')
        return int(answer)

solution = Solution()
print(solution.monotoneIncreasingDigits(1200))

class Solution:
    def numberOfSteps(self, num: int) -> int:
        answer = 0
        while num != 0:
            if num % 2 == 0:
                answer += 1
                num //= 2
            else:
                answer += 1
                num -= 1
        return answer
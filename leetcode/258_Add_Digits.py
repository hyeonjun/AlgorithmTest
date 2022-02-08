class Solution:
    def addDigits(self, num: int) -> int:
        num = list(str(num))
        while len(num) > 1:
            num = list(str(sum(map(int, num))))
        return ''.join(num)
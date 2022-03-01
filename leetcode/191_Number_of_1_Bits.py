class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            # n=XXXX1000, n-1=XXXX0111 => n & n-1 = XXXX0000
            n &= n-1
            answer += 1
        return answer
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], 2)


class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        """
        n = 1010, answer = 0
        1. answer = 0, n = 101
        2. answer = 01, n = 10
        3. answer = 010, n = 1
        4. answer = 0101, n = 0

        => 1) answer = (answer << 1) ^ (n & 1) : 마지막 비트를 answer에 추가
           2) n >>= 1 : n에서 마지막 비트 제거
        """
        for i in range(32):
            answer = (answer << 1) ^ (n & 1) # answer = (answer << 1) + (n & 1)
            n >>= 1
        return answer

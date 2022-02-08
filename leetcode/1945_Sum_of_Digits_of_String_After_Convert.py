class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = [str(ord(i)-ord('a')+1) for i in s]
        s = list(''.join(s))
        for _ in range(k):
            s = list(str(sum(map(int, s))))
        return ''.join(s)
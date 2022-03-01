class Solution: # 351ms
    def countBits(self, n: int) -> list[int]:
        answer = []
        for i in range(n+1):
            answer.append(sum(map(int, list(bin(i)[2:]))))
        return answer


class Solution: # 126ms
    def countBits(self, n: int) -> list[int]:
        answer = [0]
        for i in range(1, n + 1):
            answer.append(answer[i >> 1] + i % 2)
        return answer
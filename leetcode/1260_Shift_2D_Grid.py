class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        answer = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                answer[(i+(j+k)//m)%n][(j+k) % m] = grid[i][j]
        return answer

# Flatten
class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        n, m = len(grid), len(grid[0])
        k %= n * m
        flatten = [grid[i][j] for i in range(n) for j in range(m)]
        flatten = flatten[-k:] + flatten[:-k]
        return [[flatten[i*m+j] for j in range(m)] for i in range(n)]
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        answer = [[0 for _ in range(n)] for _ in range(n)]
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        N, num = n * n, 1
        sx, sy, ex, ey = 0, 0, n // 2, n // 2
        while True:
            answer[sx][sy] = num
            if num == N:
                break
            num += 1
            nx, ny = sx + direction[d][0], sy + direction[d][1]
            if 0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0:
                sx, sy = nx, ny
            else:
                d = (d + 1) % 4
                sx, sy = sx + direction[d][0], sy + direction[d][1]

        return answer

solution = Solution()
result = solution.generateMatrix(2)
for res in result:
    print(res)
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        r, c = len(grid), len(grid[0])
        def bfs():
            queue = [(0, 0)]
            visited = [[0 for _ in range(c)] for _ in range(r)]
            visited[0][0] = 1
            while queue:
                x, y = queue.pop(0)
                if (x, y) == (r-1, c-1):
                    return visited[x][y]
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 0 and not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
            return -1
        return bfs()
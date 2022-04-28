# BFS + Binary Search, 3071ms
from collections import deque
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(effort):
            queue = deque([(0, 0)])
            visited[0][0] = True
            while queue:
                x, y = queue.popleft()
                if (x, y) == (r - 1, c - 1):  # 가능
                    return True
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and abs(
                            heights[x][y] - heights[nx][ny]) <= effort:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False

        left, right = 0, 10 ** 6
        while left <= right:
            mid = (left + right) // 2
            visited = [[False for _ in range(c)] for _ in range(r)]
            if bfs(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# Dijkstra, 689ms
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r, c = len(heights), len(heights[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[1e9 for _ in range(c)] for _ in range(r)]

        def dijkstra():
            queue = [(0, 0, 0)]
            heapq.heapify(queue)
            visited[0][0] = 0
            while queue:
                d, x, y = heapq.heappop(queue)
                if (x, y) == (r - 1, c - 1):
                    return visited[x][y]
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        nd = max(d, abs(heights[x][y] - heights[nx][ny]))
                        if nd < visited[nx][ny]:
                            visited[nx][ny] = nd
                            heapq.heappush(queue, (nd, nx, ny))
            return 0

        return dijkstra()
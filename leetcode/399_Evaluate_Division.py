from typing import List
from collections import defaultdict


# Solution 1 - DFS
class Solution1:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(prev, nxt, value):
            if prev in visited:
                return False
            if prev == nxt and nxt in graph:
                answer.append(value)
                return True

            visited.add(prev)
            for n, v in graph[prev]:
                if dfs(n, nxt, value * v):
                    return True
            visited.remove(prev)
            return False

        answer = []
        for x, y in queries:
            visited = set()
            if not dfs(x, y, 1):
                answer.append(-1)
        return answer

# Solution 2 - BFS
class Solution2:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def bfs(start, end):
            if start not in graph and end not in graph:
                return -1
            queue = [(start, 1)]
            visited = set()
            while queue:
                x, v = queue.pop(0)
                if x == end:
                    return v
                for nx, nv in graph[x]:
                    if nx not in visited:
                        visited.add(nx)
                        queue.append((nx, v * nv))
            return -1

        return [bfs(s, e) for s, e in queries]
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        low = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        self.answer = []

        def dfs(rank, cur, prev):
            low[cur] = rank
            visited[cur] = True
            for nxt in graph[cur]:
                if nxt == prev:
                    continue
                if not visited[nxt]:
                    dfs(rank + 1, nxt, cur)
                low[cur] = min(low[cur], low[nxt])
                if low[nxt] >= rank + 1:
                    self.answer.append([cur, nxt])

        dfs(1, 0, -1)
        return self.answer
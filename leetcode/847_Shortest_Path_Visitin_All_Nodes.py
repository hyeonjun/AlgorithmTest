# BFS, BitMask
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        queue = [(x, 1 << x) for x in range(n)]
        visited = set(queue)
        answer = 1
        while queue:
            for i in range(len(queue)):
                now_n, now_v = queue.pop(0)
                for next_n in graph[now_n]:
                    next_v = now_v | (1 << next_n)
                    if next_v + 1 == 1 << n:
                        return answer
                    if (next_n, next_v) not in visited:
                        visited.add((next_n, next_v))
                        queue.append((next_n, next_v))
            answer += 1

# BFS, BitMask, DP
class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        if n == 1:
            return 0
        dp = [[float('inf')] * n for _ in range(1 << n)]
        queue = []
        for i in range(n):
            dp[1 << i][i] = 0
            queue.append((i, 1 << i))

        while queue:
            now_n, now_v = queue.pop(0)
            for next_n in graph[now_n]:
                next_v = now_v | (1 << next_n)
                if dp[next_v][next_n] == float('inf'):
                    dp[next_v][next_n] = dp[now_v][now_n] + 1
                    queue.append((next_n, next_v))
        return min(dp[-1])
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        graph = []
        for i in range(n):
            for j in range(i + 1, n):
                graph.append((i, j, abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
        graph.sort(key=lambda x: x[2])

        parent = list(range(n))

        def find(x):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a, b = find(a), find(b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        answer = 0
        for x, y, d in graph:
            if find(x) == find(y): continue
            union(x, y)
            answer += d
        return answer
# Solution 1 - Union-Find
from collections import defaultdict
from typing import List


class Solution1:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
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

        for x, y in pairs:
            union(x, y)

        dp = defaultdict(list)
        for i in range(n):
            dp[find(i)].append(s[i])

        for i in dp.keys():
            dp[i].sort(reverse=True)

        answer = ''
        for i in range(n):
            answer += dp[find(i)].pop()
        return answer

# Solution 2 - DFS
class Solution2:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        graph = [[] for _ in range(n)]
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(idx):
            visited[idx] = True
            index.append(idx)
            string.append(s[idx])
            for node in graph[idx]:
                if not visited[node]:
                    dfs(node)

        s = list(s)
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                index, string = [], []
                dfs(i)
                index.sort();
                string.sort()
                for idx in range(len(index)):
                    s[index[idx]] = string[idx]
        return ''.join(s)
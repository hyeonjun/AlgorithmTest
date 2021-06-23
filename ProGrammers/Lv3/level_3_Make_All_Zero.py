# -*- coding:cp949 -*-
import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

def solution(a, edges):
    global answer
    answer = 0
    if sum(a) != 0:
        return -1

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(u, v):
        global answer
        for node in graph[u]:
            if node != v:
                dfs(node, u)

        answer += abs(a[u])
        a[v] += a[u]
        a[u] = 0

    dfs(0, 0)
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9

def solution(a, edges):
    global answer
    answer = 0

    if sum(a) != 0:
        return -1

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * len(a)

    def dfs(x):
        global answer
        visited[x] = 1
        for y in graph[x]:
            if not visited[y]:
                a[x] += dfs(y)
        answer += abs(a[x])
        return a[x]

    dfs(0)
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]])) # 9
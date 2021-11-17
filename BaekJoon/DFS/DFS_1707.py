# 이분 그래프 판별
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def dfs(x, i):
    visited[x] = i
    for dx in graph[x]:
        if not visited[dx]:
            if not dfs(dx, -i): # 1과 -1로 색 구분 -> 이분 그래프
                return False
        # 방문한 곳이면서 같은 그룹이면 False
        elif visited[dx] == visited[x]:
            return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(v + 1)]
    result = True
    for i in range(1, v+1):
        if not visited[i] and not dfs(i, 1):
            result = False
            break
    if result:
        print("YES")
    else:
        print("NO")
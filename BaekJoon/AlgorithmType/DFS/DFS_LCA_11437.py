import sys
sys.setrecursionlimit(10 ** 5)

n = int(input())
parent = [0 for _ in range(n+1)] # 부모 노드 정보
level = [0 for _ in range(n+1)] # 각 노드까지의 깊이
visited = [False for _ in range(n+1)] # 깊이 계산 여부

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트부터 깊이 구하기 - 트리
def dfs(x, depth):
    visited[x] = True
    level[x] = depth

    # 현재 노드와 연결되어 있는 노드 확인
    for i in graph[x]:
        if not visited[i]:
            parent[i] = x
            dfs(i, depth+1)

# 최소 공통 조상 찾기
def LCA(a, b):
    # 레벨 맞추기 - 깊이가 동일하도록 함
    while level[a] != level[b]:
        if level[a] > level[b]:
            a = parent[a]
        else:
            b = parent[b]

    # a와 b의 공통 조상 찾기 - 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))

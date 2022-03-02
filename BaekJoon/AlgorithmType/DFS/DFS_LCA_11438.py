"""
최대 100,000개의 정점이 입력으로 들어올 수 있다.
그렇다면 일반적인 LCA 알고리즘으로 해결할 수 없다.
 ->부모 노드를 찾는 것에 더 빠른 알고리즘이 필요

노드마다 깊이와 2^i(i=0, 1, 2)번째 부모에 대한 정보를 저장하여
2의 제곱꼴로 이동하면서 최소 공통 조상을 찾도록 한다.
시간 복잡도 - O(logN)
"""

import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline
LOG = 21 # 2 ** 20 = 1,000,000

n = int(input())
# 부모 노드 정보 - parent[i][j] => i번 노드의 j번 째 부모 = 부모 노드
parent = [[0] * LOG for _ in range(n+1)]
level = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    visited[x] = True
    level[x] = depth
    for i in graph[x]:
        if not visited[i]:
            parent[i][0] = x # 한칸 위 부모 정보만 저장
            dfs(i, depth+1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1, 0)
    for j in range(1, LOG):
        for i in range(1, n+1):
            # 2의 제곱꼴로 부모 노드 정보를 저장한다 - 1, 2, 4, 8, ... 번재 부모 노드
            parent[i][j] = parent[parent[i][j-1]][j-1]

def LCA(a, b):
    # 무조건 b가 더 깊도록 설정
    if level[a] > level[b]:
        a, b = b, a

    # 레벨 맞추기 - 깊이가 동일하도록
    for i in range(LOG-1, -1, -1):
        # 깊이의 차이가 15일 때, 8 4 2 1(2의 제곱꼴만큼 감소)로 줄어들 수
        # 있도록 하여 총 4번만에 같아지도록 한다.
        if level[b] - level[a] >= (1 << i):
            b = parent[b][i] # 더 깊은 b의 깊이가 줄어들도록 한다

    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        # 조상을 향해 거슬러 올라간다
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

set_parent()
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(LCA(a, b))

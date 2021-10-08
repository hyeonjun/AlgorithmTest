import sys
sys.setrecursionlimit(1000000)
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    tree[a].append((d, b)) # 가중치, 자식노드
    tree[b].append((d, a))

def dfs(x):
    for v, i in tree[x]:
        if distances[i] == 0:
            distances[i] = distances[x] + v
            dfs(i)

distances = [0 for _ in range(n+1)]
dfs(1)
x = distances.index(max(distances)) # 임의의 정점 x에서 가장 먼 정점 구함

distances = [0 for _ in range(n+1)]
dfs(x)
distances[x] = 0

print(max(distances))
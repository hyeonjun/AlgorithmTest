# 트리의 지름 구하기 = 가장 먼 두 정점의 거리 = 가장 먼 두 정점을 연결하는 경로
# 1. 트리에서 임의의 정점 x를 잡는다.
# 2. 정점 x에서 가장 먼 정점 y를 찾는다.
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.
# 트리의 지름은 정점 y와 정점 z를 연결하는 경로.

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int, input().split()))
    for i in range(1, len(tmp)-2, 2):
        tree[tmp[0]].append((tmp[i], tmp[i+1])) # 연결된 정점과 거리

def dfs(x):
    for i, v in tree[x]:
        if result1[i] == 0:
            result1[i] = result1[x] + v
            dfs(i)

result1 = [0 for _ in range(v+1)]
dfs(1)

node = result1.index(max(result1)) # 임의의 정점 x에서 가장 먼 정점 구함
result1 = [0 for _ in range(v+1)]
dfs(node)

result1[node] = 0
print(max(result1))
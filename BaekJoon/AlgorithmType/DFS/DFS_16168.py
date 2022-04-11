from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 5)
v, e = map(int, input().split())
graph = defaultdict(list)
count = [0 for _ in range(v+1)]
visited = [0 for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    count[a] += 1
    count[b] += 1
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)

odd = 0 # 차수가 홀수인 정점 체크
for i in range(1, v+1):
    if count[i] % 2:
        odd += 1

# 차가 홀수인 정점이 2개 이하면 오일러 경로 조건 만족
if odd <= 2:
    visited[1] = 1
    dfs(1)
    if sum(visited) == v: # 모든 정점을 방문하는지 확인
        print("YES")
    else:
        print("NO")
else:
    print("NO")
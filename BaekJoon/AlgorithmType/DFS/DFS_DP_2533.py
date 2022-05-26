import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
"""
dp[i][0]: i번 노드가 얼리아답터가 아닐 때 서브 트리에서 얼리아답터 최소 개수
dp[i][1]: i번 노드가 얼리아답터일 때 서브 트리에서 얼리아답터 최소 개수
a가 부모, b, c를 자식노드라 했을 때,
1. a가 얼리아답터일 경우, b, c는 얼리아답터여도 되고 아니여도 됨
2. b, c 중 하나라도 얼리아답터가 아닐 경우 무조건 a는 얼리아답터여야 한다.
  => a가 얼리아답터가 아니라면? b, c는 모두 얼리아답터여야 하는 것
"""
dp = [[0, 1] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

def dfs(idx):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            dfs(i) # 제일 아래 child 부터 root 까지 올라가면서 계산
            # idx번 노드가 얼리아답터가 아니라면, 자식 노드는 무조건 얼리아답터
            dp[idx][0] += dp[i][1]
            # idx번 노드가 얼리아답터라면, 자식 노드는 얼리아답터여도 되고 아니여도 됨
            # => 얼리아답터 개수가 더 작은 케이스를 가져옴
            dp[idx][1] += min(dp[i][0], dp[i][1])

dfs(1) # 시작점은 어디를 선택해도 상관없음
print(min(*dp[1])) # 두 가지 케이스 중 적은 케이스를 선택
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global answer
    visited[x] = True
    route.append(x)
    nx = num[x]

    if not visited[nx]:
        dfs(nx)
    else: # 이미 방문한 곳이면 사이클이 되는지 확인
        if nx in route: # 탐색한 경로에 nx가 들어가 있으면 사이클이 되었다는 뜻
            answer += route[route.index(nx):] # 사이클이 되는 순간부터 answer에 넣음

for _ in range(int(input())):
    n = int(input())
    num = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    answer = set() # 사이클

    for i in range(1, n+1):
        if not visited[i]:
            route = [] # 탐색 경로
            dfs(i)

    print(n - len(answer))
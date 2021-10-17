import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0]+list(map(int, input().split())) # 각 건물들의 건설 시간 (1~N)
    graph = [[] for _ in range(n+1)] # 건물 순서 규칙
    degree = [0 for _ in range(n+1)] # 진입차수
    dp = [0 for _ in range(n+1)] # 해당 건물까지 걸리는 시간
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1

    queue = []
    for i in range(1, n+1): # 진입 차수 0 -> 시작
        if degree[i] == 0:
            queue.append(i)
            dp[i] = d[i] # 건물 건설 걸리는 시간 추가

    while queue:
        x = queue.pop(0)
        for i in graph[x]:
            degree[i] -= 1 # 선택된 정점에 부속된 모든 간선에 대해 진입차수 줄임 -> 다음 0인 것을 찾아서 큐에 넣어야함
            dp[i] = max(dp[x]+d[i], dp[i]) # 건설 시간 갱신
            if degree[i] == 0:
                queue.append(i)

    w = int(input())
    print(dp[w])

import heapq, sys
input=sys.stdin.readline
n, m = map(int, input().split())
price = [0]+list(map(int, input().strip().split())) # c
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))
    graph[b].append((d, a))

def dijkstra():
    # [현재 위치 n][현재 가장 싼 기름값 c] = 총 비용 d
    # 1e9는 부족하기 때문에 float('inf')로 초기화해야한다.
    dp = [[float('inf') for _ in range(max(price)+1)] for _ in range(n+1)]
    dp[1][price[1]] = 0
    queue = []
    heapq.heappush(queue, [0, price[1], 1]) # 총 비용 d, 현재까지 가장 싼 주유소 c, 현재 위치 n
    while queue:
        # 현재 총 비용, 현재 주요소 비용, 현재 위
        now_d, now_c, now_n = heapq.heappop(queue)
        if now_n == n: # 도착
            return now_d
        if dp[now_n][now_c] < now_d:
            continue
        for next_d, next_n in graph[now_n]:
            # 다음 정점에서 쓸 비용
            next_c = min(price[next_n], now_c)
            # 현재 위치에서 다음 위치로 이동할 때 드는 비용
            next_d = now_d + now_c * next_d
            if next_d < dp[next_n][now_c]:
                dp[next_n][now_c] = next_d
                heapq.heappush(queue, (next_d, next_c, next_n))

print(dijkstra())

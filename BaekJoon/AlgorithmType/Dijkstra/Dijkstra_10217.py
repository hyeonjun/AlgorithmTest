import heapq
import sys
input = sys.stdin.readline
def dijkstra():
    queue = [(0, 0, 1)] # 시간, 비용, 출발
    heapq.heapify(queue)
    # DP[위치][비용] = 소요 시간
    dp = [[1e9 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][0] = 0

    while queue:
        now_d, now_c, now_n = heapq.heappop(queue)
        if dp[now_n][now_c] < now_d:
            continue
        for next_n, next_c, next_d in graph[now_n]:
            next_c += now_c
            next_d += now_d
            # 가능한 비용이면서 시간이 짧은 경우
            if next_c <= m and next_d < dp[next_n][next_c]:
                # 더 높은 비용을 투자하면서 시간이 긴 모든 것들을 업데이트
                for c in range(next_c, m+1):
                    if next_d < dp[next_n][c]:
                        dp[next_n][c] = next_d
                    else:
                        break
                heapq.heappush(queue, (next_d, next_c, next_n))

    return dp


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    dp = dijkstra()
    print(dp[n][m] if dp[n][m] != 1e9 else 'Poor KCM')
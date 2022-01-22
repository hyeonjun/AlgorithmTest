"""
- 외판원 순회 - TSP
1~N번까지의 도시들이 있고, 도시들 사이에는 길이 있을 수도 없을 수도 있다.
어느 한 도시에서 출발하여 N개의 도시를 모두 거쳐 다시 원래 도시로 돌아오는 순회. -> DFS
처음 도시로 돌아오는 것을 제외하고 한번 갔던 도시로는 다시 못간다. -> 비트마스킹
가장 적은 비용을 들이고 순회. -> DP

- 비트마스킹
0001(2) => 0번 도시 거침
0011(2) => 0, 1번 도시 거침
0111(2) => 0, 1, 2번 도시 거침
1111(2) => 0, 1, 2, 3번 도시 거침

- DP[cur][visit] : 현재 도시 cur, 방문 현황 visit 일 때, 아직 방문하지 않은 도시들을 모두 거쳐 다시 돌아가는데 드는 최소 비용
ex) dp[0][0011(2)] = dp[0][3] = 현재 0번 도시, 0, 1번 도시를 방문하였을 때 // 남은 2, 3번의 도시를 모두 거쳐 다시 돌아가는데 드는 최소 비용
    dp[2][0111(2)] = dp[2][7] = 현재 2번 도시, 0, 1, 2번 도시를 방문 하였을 때 // 남은 3번 도시를 거쳐 다시 돌아가는데 드는 최소 비용
    => dp[0][3] : 2, 3번을 거쳐서 돌아 가는데 드는 비용
       dp[2][7] : 3번을 거쳐서 돌아 가는데 드는 비용
       => dp[0][3] = dp[2][7] + graph[0][2](0에서 2로 이동하는데 드는 비용)
           => dp[cur][visit] = min(dp[cur][visit], dp[nxt][nxtvisit] + graph[cur][nxt])
                => dp[cur][visit] = min(dp[cur][visit], dp[nxt][visit | (1 << nxt)] + graph[cur][nxt])
- DFS로 DP 갱신
dp[cur][visit] = min(dp[cur][visit], dp[nxt][visit | (1 << nxt)] + graph[cur][nxt])
 => dp[cur][visit] = min(dp[cur][visit], dfs(nxt, visit | (1 << nxt)) + graph[cur][nxt])
"""
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e9 for _ in range(1 << n)] for _ in range(n)]

def dfs(cur, visit):
    if visit == (1 << n)-1: # 모든 도시 방문
        return graph[cur][0] or 1e9 # 출발점으로 가는 경로가 있으면 graph[cur][0], 없으면 1e9
    if dp[cur][visit] != 1e9: # 이미 최소 비용이 계산되었다면
        return dp[cur][visit] # 최소 비용 반환

    for nxt in range(1, n): # 모든 도시 순회
        if not graph[cur][nxt] or visit & (1 << nxt): # 가는 길이 없거나 이미 방문한 도시면 패스
            continue
        dp[cur][visit] = min(dp[cur][visit], dfs(nxt, visit | (1 << nxt)) + graph[cur][nxt])
    return dp[cur][visit]

print(dfs(0, 1 << 0))






















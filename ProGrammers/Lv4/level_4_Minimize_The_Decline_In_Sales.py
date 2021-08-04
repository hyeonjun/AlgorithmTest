import math
def solution(sales, links):  # DP + DFS
    child = [[] for _ in range(300000)]
    for i in links:
        child[i[0] - 1].append(i[1] - 1)

    dp = [[0, 0] for _ in range(300000)]

    def dfs(node):
        dp[node][0] = 0
        dp[node][1] = sales[node]

        # 현재 노드가 리프 노드인가
        if not child[node]:
            return

        # 아니라면 자식 노드 순회
        ex_cost = math.inf  # 추가 비용
        for c in child[node]:
            dfs(c)
            if dp[c][0] < dp[c][1]:
                dp[node][0] += dp[c][0]
                dp[node][1] += dp[c][0]
                ex_cost = min(ex_cost, dp[c][1] - dp[c][0])  # 모든 자식이 참가하지 않았다면
            else:
                dp[node][0] += dp[c][1]
                dp[node][1] += dp[c][1]
                ex_cost = 0  # 자식 중에 하나라도 참가한다면 추가 비용은 필요 없음
        dp[node][0] += ex_cost

    dfs(0)
    return min(dp[0][0], dp[0][1])

# 44
print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
# 6
print(solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
# 5
print(solution([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
# 2
print(solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]))
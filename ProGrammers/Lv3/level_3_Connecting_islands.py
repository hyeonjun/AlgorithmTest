def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2]) # 비용기반 정렬
    routes = {costs[0][0]} # set([costs[0][0]])
    while len(routes) != n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]]) # 두 개 값 넣기
                answer += cost[2]
                costs[i] = [-1,-1,-1] # 이미 넣은 것은 없앰
                break
    return answer

# 15
print(solution(5,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
print(solution(5, [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]])) # 8
print(solution(4, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]])) # 9
# 104
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]))
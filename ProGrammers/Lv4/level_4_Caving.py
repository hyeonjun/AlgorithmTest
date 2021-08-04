def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)

    orders = [0 for _ in range(n)]
    for pre, post in order:
        orders[post] = pre  # [방문할 방] = 이전에 방문할 방

    visit_n = 0  # 방문한 방 수
    visited = [False for _ in range(n)]  # 방문 체크

    queue = [0]  # 0번 먼저
    after = {}  # 방문해야할 노드 : key 노드를 들른 후 갈 수 있는 노드

    while queue:
        x = queue.pop(0)
        if orders[x] and not visited[orders[x]]:
            after[orders[x]] = x
            continue

        visited[x] = True
        visit_n += 1
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)

        if x in after:
            queue.append(after[x])

    return n == visit_n

# true
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
# true
print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
# false
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
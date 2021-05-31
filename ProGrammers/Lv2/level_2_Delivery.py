def solution(N, road, K): # 다익스트라
    from collections import defaultdict
    graph = defaultdict(list)
    distances = {node: float('inf') if node != 1 else 0 for node in range(1, N + 1)}
    for n1, n2, d in road:
        graph[n1].append((n2, d))
        graph[n2].append((n1, d))

    queue = [1]
    while queue:
        cur_n = queue.pop(0)
        for next_node, d in graph[cur_n]:
            distance = distances[cur_n] + d
            if distances[next_node] > distance:
                distances[next_node] = distance
                queue.append(next_node)
    return len([i for i in distances.values() if i <= K])

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4
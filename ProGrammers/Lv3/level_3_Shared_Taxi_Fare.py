def solution(n, s, a, b, fares):
    import heapq
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    for src, dst, cost in fares:
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])

    def dijkstra(src, dst):
        distance = [1e9] * len(graph)
        distance[src] = 0
        heap = []
        heapq.heappush(heap, (0, src))

        while heap:
            cost, now = heapq.heappop(heap)
            if distance[now] < cost:
                continue
            for i in graph[now]:
                ncost = cost + i[1]
                if distance[i[0]] > ncost:
                    distance[i[0]] = ncost
                    heapq.heappush(heap, (ncost, i[0]))
        return distance[dst]

    for i in range(1, n + 1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
    return answer

fares1 = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
fares2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
fares3 = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
print(solution(6,4,6,2,fares1)) # 82
print(solution(7,3,4,1,fares2)) # 14
print(solution(6,4,5,6,fares3)) # 18
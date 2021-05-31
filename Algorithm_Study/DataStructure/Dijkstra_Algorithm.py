# -*- coding:utf-8 -*-
# Priority Queue with heapq
import heapq
queue = []
heapq.heappush(queue, [2,'A'])
heapq.heappush(queue, [5,'B'])
heapq.heappush(queue, [1,'C'])
heapq.heappush(queue, [7,'D'])
print(len(queue), queue)

for _ in range(len(queue)):
    print(heapq.heappop(queue))

# Dijkstra Algorithm
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start):
    distances = {node:float('inf') for node in graph}
    print(distances)
    distances[start] = 0
    queue = []

    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        # if distances[current_node] < current_distance:
        #     continue
        if distances[current_node] >= current_distance:
            for adjacent, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heapq.heappush(queue, [distance, adjacent])
    print(queue)
    return distances

print(dijkstra(mygraph, 'A'))

# 출발과 도착 지점을 인수로 받음
def dijkstra_algorithm(graph, start, end):
    # 시작 정점에서 각 정점까지의 거리를 inf로 초기화
    # {'A': [inf, 'A'], 'B': [inf, 'A'], 'C': [inf, 'A'], 'D': [inf, 'A'], 'E': [inf, 'A'], 'F': [inf, 'A']}
    distances = {i:[float('inf'), start] for i in graph}

    # 그래프의 시작 정점의 거리는 0으로 초기화
    distances[start] = [0, start]

    # 모든 정점을 저장할 큐
    queue = []

    # 그래프의 시작 정점과 시작 정점의 거리(0)을 최소힙에 넣어줌
    heapq.heappush(queue, [distances[start][0], start]) # [[0, 'A']]

    while queue:
        # 큐에서 정점을 하나씩 꺼내 인접한 정점들의 가중치를 모두 확인하여 업데이트
        current_distance, current_node = heapq.heappop(queue)

        # 더 짧은 경로가 이미 입력되어 있으면 무시
        if distances[current_node][0] < current_distance:
            continue
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다 현재 정점을 통해 가는 것이 더 빠르면
            if distance < distances[adjacent][0]:
                # 거리 업데이트
                distances[adjacent] = [distance, current_node]
                heapq.heappush(queue, [distance, adjacent])

    path = end
    path_output = end
    while distances[path][1] != start:
        path_output = distances[path][1] + '->' + path_output
        path = distances[path][1]
    path_output = start + '->' + path_output
    print(path_output)
    return distances

print(dijkstra_algorithm(mygraph, 'A', 'F'))
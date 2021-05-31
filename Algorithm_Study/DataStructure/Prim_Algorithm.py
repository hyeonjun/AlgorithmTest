"""
프림 알고리즘 - 최소 신장 트리 알고리즘
1. 시작 정점을 선택한 후, 정점에 인접한 간선 중 최소 간선으로 연결된 정점을 선택하고,
   해당 정점에서 다시 최소 간선으로 연결된 정점을 선택하는 방식으로 트리를 확장
2. 크루스칼과 프림 비교
 - 둘 다 탐욕 알고리즘을 기초로 하고 있다
 - 크루스칼 알고리즘은 가장 가중치가 작은 간선부터 선택하면서 MST를 구함
 - 프림 알고리즘은 특정 정점에서 시작, 해당 정점에 연결된 가장 가중치가 작은 간선을 선택,
   간선으로 연결된 정점들에 연결된 간선중에 가장 가중치가 작은 간선을 선택하는 방식으로 MST를 구함
"""

# # 우선순위 큐 사용
import heapq
# graph = []
# graph_data = [[2,'A'],[5,'B'],[3,'C']]
# for i in graph_data:
#     heapq.heappush(graph, i)
#
# print(graph) # [[2, 'A'], [5, 'B'], [3, 'C']]
#
# for i in range(len(graph)):
#     print(heapq.heappop(graph))
# # [2, 'A']
# # [3, 'C']
# # [5, 'B']
#
# # heapq.heapify() 함수를 사용해 리스트 데이터를 heap 형태로 한 번에 변환 가능
# heapq.heapify(graph_data)
# for i in range(len(graph_data)):
#     print(heapq.heappop(graph_data))
#
#
# # collections의 defaultdict 함수 - key에 대한 value를 지정하지 않았을 시, 빈 리스트로 초기화
from collections import defaultdict
list_dict = defaultdict(list)
print(list_dict['key1']) # []

list_dict = defaultdict(int)
print(list_dict['key1']) # 0

list_dict = defaultdict(float)
print(list_dict['key1']) # 0.0

print(list_dict)

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

def prim(start_node, edges):
    mst = list()
    edge_list = defaultdict(list)
    for weight, n1, n2 in edges: # 모든 간선 정보를 저장
        edge_list[n1].append((weight,n1,n2))
        edge_list[n2].append((weight,n2,n1))

    print(edge_list)

    connected_nodes = set(start_node) # 임의의 정점 선택
    candidate_edge = edge_list[start_node] # 선택된 정점에 연결된 간선들 저장
    heapq.heapify(candidate_edge)

    while candidate_edge:
        weight, n1, n2 = heapq.heappop(candidate_edge) # 간선 리스트에서 최소 가중치 간선 추출
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight,n1,n2))

            for edge in edge_list[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge, edge)
    return mst

print(prim('A', myedges))



"""
개선된 프림 알고리즘
1. 간선이 아닌 노드를 중심으로 우선순위 큐를 적용
 - 초기화 - 정점: key 구조를 만들어놓고, 특정 정점의 key값은 0, 이외의 정점들의 key값은 무한대
           모든 정점: key 같은 우선순위 큐에 넣음
 - 가장 key값이 작은 정점 : key를 추출(pop)
 - 해당 정점의 인접한 정점들에 대해 key 값과 연결된 가중치 값을 비교하여 key값이 작으면 해당 정점
    : key값을 갱신
     - 정점 : key 값 갱신 시, 
       우선순위 큐는 최소 key값을 가지는 정점: key를 루트노드로 올려놓도록 재구성
2. 개선된 프림 알고리즘 구현 시 고려사항
 - 우선순위 큐(최소힙) 구조에서 이미 들어가 있는 데이터의 값 변경 시, 최소값을 가지는 데이터를
   루트노드로 올려놓도록 재구성하는 기능 필요
 - 구현 복잡도를 줄이기 위해, heapdict 라이브러리 사용
"""
from heapdict import heapdict
def improved_prim(graph, start): # 시간 복잡도 : O(V + VlogV ElogV), E>V(최대 V^2 = E) 이므로 O(ElogV)
#   pi : 키값을 갱신할 때 어디서 온 것인지 저장
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key
        for node, weight in myedges[current_node].items():
            if node in keys and weight < keys[node]:
                keys[node] = weight
                pi[node] = current_node
    return mst, total_weight

myedges = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

mst, weight = improved_prim(myedges, 'A')
print('MST : ', mst)
print('Total Weight : ', weight)

















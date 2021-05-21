"""
크루스칼 알고리즘 - 최소 신장 트리 알고리즘
1. 모든 정점을 독집적인 집합으로 만든다.
2. 모든 간선의 비율을 기준으로 정렬하고, 비율이 작은 간선부터 양 끝의 두 정점을 비교
3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결
(주의! 최소 신장 트리는 사이클이 있으면 안된다.)
 - 탐욕 알고리즘을 기초로 하고 있다.
"""

"""
사이클 판별 방법 - Union Find
1. Disjoint Set을 표현할 때 사용하는 알고리즘으로 트리 구조를 활용하는 알고리즘
2. 노드들 중에 연결된 노드를 찾거나, 노드들을 서로 연결할 때(합칠 때) 사용
 * Disjoint Set이란
  - 서로 중복되지 않는 부분 집합들로 나눠진 원소들에 대한 정보를 저장하고 조작하는 자료구조
  - 공통 원소가 없는(서로소) 상호 배타적인 부분 집합들로 나눠진 원소들에 대한 자료구조
  - Disjoint Set = 서로소 집합 자료구조 
3. 고려할 점
 - Union 순서에 따라서, 최악의 경우 링크드 리스트와 같은 형태가 될 수 있다.
 - 이 때는 Find/Union 시 계산량이 O(N)이 될 수 있음, 해당 문제를 해결하기 위해
   union-by-rank, path compresstion 기법을 사용함
"""

"""
union-by-rank
1. 각 트리에 대해 높이(rank)를 기억.
2. Union시 두 트리의 높이(rank)가 다르면, 높이가 작은 트리를 높이가 큰 트리에 붙임
(즉, 높이가 큰 트리의 루트 노드가 합친 집합의 루트 노드가 되게 함)
3. 높이가 h-1인 두개의 트리(즉, 높이가 같은 두 트리)를 합칠 때는 한 쪽의 트리 높이를 1 증가.
   그 후 다른 쪽의 트리를 해당 트리에 붙임
4. 초기화 시, 모든 원소는 높이(rank)가 0인 개별 집합인 상태에서 하나씩 원소를 합칠 때 Union-by-rank 기법을 사용한다면,
 - 높이가 h인 트리가 만들어지려면, 높이가 h-1인 두 개의 트리가 합쳐야함
 - 높이가 h-1인 트리를 만들기 위해 최소 n개의 원소가 필요하다면, 
   높이가 h인 트리가 만들어지기 위해서는 최소 2n개의 원소 필요
 - 따라서 union-by-rank 기법을 사용하면, union-find 연산의 시간복잡도는 O(N)이 아닌 O(logN)로 낮출 수 있음
"""

"""
path compression
1. Find를 실행한 노드에서 거쳐간 노드를 루트에 다이렉트로 연결하는 기법
2. Find를 실행한 노드는 이후부터는 루트 노드를 한번에 알 수 있음
"""

"""
*** union-by-rank와 path compression 기법 사용 시 시간 복잡도는 다음 계산식을 만족
 - O(M*logN)
 - 
"""

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()
class Kruskal():
    def __init__(self, graph):
        self.graph = graph
        self.parent = dict()
        self.rank = dict()

    def kruskals_UnionFind(self):
        def find(node):
            # Path Compression
            if parent[node] != node:  # 부모 노드 찾기
                parent[node] = find(parent[node])
            return parent[node]  # 루트노드

        def union(node_v, node_u):
            root1 = find(node_v)
            root2 = find(node_u)

            # union-by-rank
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2

                if rank[root1] == rank[root2]:
                    rank[root2] += 1

        def make_set(node):
            parent[node] = node
            rank[node] = 0

        mst = list()

        # 1. 초기화
        for node in self.graph['vertices']:
            make_set(node)

        # 2. 간선 weight기반 sort
        edges = self.graph['edges']
        edges.sort()

        # 3. 간선 연결(사이클이 없는)
        for edge in edges:
            weight, node_v, node_u = edge
            if find(node_v) != find(node_u):
                union(node_v, node_u)
                mst.append(edge)
        return mst

kruskal = Kruskal(graph)
print(kruskal.kruskals_UnionFind())
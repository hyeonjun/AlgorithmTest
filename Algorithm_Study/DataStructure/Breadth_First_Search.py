# 너비 우선 탐색(Breadth_First_Search
# 정점들과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식
# 시간 복잡도(노드 수:V, 간선 수: E) : O(V+E)

def bfs(graph, start_node):
    visited, need_visit = [], [start_node]

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

print(bfs(graph, 'A')) # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']

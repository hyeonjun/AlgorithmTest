# 깊이 우선 탐색(Depth_First_Search)
# 정점의 자식들을 먼저 탐색하는 방식
# 시간 복잡도(노드 수:V, 간선 수: E) : O(V+E)

def dfs_left(graph, start_node):
    visited, need_visit = list(), list()
    visited.append(start_node)

    need_visit.extend(graph[start_node])
    node = need_visit.pop(0)
    visited.append(node)
    need_visit.extend(graph[node])

    while need_visit:
        node = need_visit.pop(1) if len(need_visit) > 1 else need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


def dfs_right(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
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
print(dfs_left(graph, 'A'))
print(dfs_right(graph, 'A'))
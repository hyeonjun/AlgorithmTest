# 카카오 2022 블라인드 5번
def solution(info, edges):
    global answer
    graph = [[] for _ in range(len(info))]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    answer = 0

    def dfs(node_set, wolf, sheep):
        global answer
        answer = max(answer, sheep)
        for node in node_set:
            for adj in graph[node]:
                if adj in node_set:
                    continue
                if info[adj] == 0:
                    node_set.add(adj)
                    dfs(node_set, wolf, sheep+1)
                    node_set.remove(adj)
                else:
                    if sheep > wolf+1:
                        node_set.add(adj)
                        dfs(node_set, wolf+1, sheep)
                        node_set.remove(adj)
    dfs(set([0]), 0, 1)
    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
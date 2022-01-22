# 카카오 2022 블라인드 5번
def solution(info, edges):
    global answer
    graph = [[] for _ in range(len(info))]
    for x, y in edges:
        graph[x].append(y)
    answer = 0

    def dfs(node, wolf, sheep):
        global answer
        answer = max(answer, sheep)

        for n in node:
            for adj in graph[n]:
                if adj in node or (info[adj] == 1 and sheep <= wolf+1):
                    continue
                node.add(adj)
                if info[adj] == 0:
                    dfs(node, wolf, sheep+1)
                else:
                    dfs(node, wolf+1, sheep)
                node.remove(adj)

    dfs(set([0]), 0, 1)
    return answer

print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1], [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
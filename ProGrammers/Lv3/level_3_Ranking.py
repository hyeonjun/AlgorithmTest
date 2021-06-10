def solution(n, results):
    answer = 0
    graph = [[None for _ in range(n)] for _ in range(n)]
    for w, l in results:
        graph[w-1][l-1] = True # win
        graph[l-1][w-1] = False # lose
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] == None:
                    continue
                # j -> i -> k
                # if j-> i한테 이기고 i가 k한테 이기면 j도 k를 이김
                # 그 반대 상황도 마찬가지.
                if graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = graph[i][j]
    for i in range(n):
        if None in graph[i][:i] + graph[i][i+1:]: # 본인 인덱스를 제외한 다른 부분에 None이 있으면 순위 알수없음
            continue
        answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2

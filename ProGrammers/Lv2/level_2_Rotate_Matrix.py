def solution(rows, columns, queries):
    answer = []
    array = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    for x1, y1, x2, y2 in queries:
        tmp = array[x1 - 1][y1 - 1]
        minV = tmp

        # 왼쪽 세로
        for i in range(x1 - 1, x2 - 1):
            t = array[i + 1][y1 - 1]
            array[i][y1 - 1] = t
            minV = min(minV, t)

        # 하단 가로
        for i in range(y1 - 1, y2 - 1):
            t = array[x2 - 1][i + 1]
            array[x2 - 1][i] = t
            minV = min(minV, t)

        # 오른쪽 세로
        for i in range(x2 - 1, x1 - 1, -1):
            t = array[i - 1][y2 - 1]
            array[i][y2 - 1] = t
            minV = min(minV, t)

        # 상단 가로
        for i in range(y2 - 1, y1 - 1, -1):
            t = array[x1 - 1][i - 1]
            array[x1 - 1][i] = t
            minV = min(minV, t)

        array[x1 - 1][y1] = tmp
        answer.append(minV)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])) # [8, 10, 25]
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])) # [1, 1, 5, 3]
print(solution(100,97,[[1,1,100,97]])) # [1]
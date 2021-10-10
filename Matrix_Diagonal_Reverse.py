# 행렬 대각선 반전
from copy import deepcopy
def diagonal(matrix, r1, c1, r2, c2, typ):
    n, m = r2 - r1+1, c2 - c1+1
    diagona = [[] for _ in range(m + n - 1)]
    if typ == 1:
        for i in range(n):
            for j in range(m):
                diagona[i + j].append((i+r1, j+c1))
    else:
        for i in range(n):
            for j in range(m):
                diagona[i - j + m - 1].append((i+r1, j+c1))

    matrix_reverse = deepcopy(matrix)
    for i in diagona:
        idx = len(i) - 1
        for j in range(len(i) // 2):
            matrix_reverse[i[idx][0]][i[idx][1]] = matrix[i[j][0]][i[j][1]]
            matrix_reverse[i[j][0]][i[j][1]] = matrix[i[idx][0]][i[idx][1]]
            idx -= 1

    return matrix_reverse

matrix = [[6 * j + i for i in range(6)] for j in range(6)]
for i in matrix:
    for j in i:
        print(j, end="\t")
    print()
print()

# 1 -> 왼쪽 아래 대각선 기준, -1 -> 오른쪽 아래 대각선 기준
queries = [[2,1,4,3,1], [1,0,4,5,-1], [0,0,5,5,1], [1,1,4,4,-1]]
for r1, c1, r2, c2, typ in queries:
    matrix = diagonal(matrix, r1, c1, r2, c2, typ)
    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()
    print()
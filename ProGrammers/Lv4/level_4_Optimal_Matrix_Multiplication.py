def solution(matrix_sizes):
    table = [[float('inf') for _ in range(len(matrix_sizes))] for _ in range(len(matrix_sizes))]

    for i in range(len(matrix_sizes)):
        table[i][i] = 0  # 곱셈 불가한 경우는 0

    for i in range(1, len(matrix_sizes)):
        for start in range(len(matrix_sizes)):
            end = start + i
            if end >= len(matrix_sizes):
                break
            for fixed in range(start, end):
                table[start][end] = min(
                    table[start][end],
                    table[start][fixed] + table[fixed + 1][end] + (
                                matrix_sizes[start][0] * matrix_sizes[fixed + 1][0] * matrix_sizes[end][1])
                )
    return table[0][-1]

print(solution([[5,3],[3,10],[10,6]])) # 270
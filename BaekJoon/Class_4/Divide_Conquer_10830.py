n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
def matrix_mul(m1, m2):
    return [[sum(i*j for i,j in zip(row_a, column_b)) % 1000 for column_b in zip(*m2)] for row_a in m1]

# AAAAA -> (A^2)^2 * A
# AAAA -> (A^2)^2

def divide(mtx, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                mtx[i][j] %= 1000
        return mtx
    elif b%2 == 1: # 홀수
        result = divide(mtx, b-1)
        new_mtx = matrix_mul(mtx, result) # 마지막에 짝수제곱한 결과와 원래 Matrix를 곱하면 홀수 제곱이 된다
        return new_mtx
    else:
        result = divide(mtx, b//2)
        new_mtx = matrix_mul(result, result) # 짝수 제곱
        return new_mtx

answer = divide(matrix, m)
for i in answer:
    print(*i)
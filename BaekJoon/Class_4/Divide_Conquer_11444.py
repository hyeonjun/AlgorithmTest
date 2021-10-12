"""
- 행렬 곱셈을 활용한 풀이, O(log2_N)
n번째 피보나치 수 = Fn
(Fn+1 Fn   )    =  (1 1)^n
(Fn   Fn-1 )       (1 0)
"""
n = int(input())

def matrix_mul(m1, m2):
    return [[sum(i*j for i,j in zip(row_a, column_b)) % 1000000007 for column_b in zip(*m2)] for row_a in m1]

def divide(mtx, b):
    if b == 1:
        for i in range(2):
            for j in range(2):
                mtx[i][j] %= 1000000007
        return mtx
    elif b%2 == 1: # 홀수
        result = divide(mtx, b-1)
        new_mtx = matrix_mul(mtx, result) # 마지막에 짝수제곱한 결과와 원래 Matrix를 곱하면 홀수 제곱이 된다
        return new_mtx
    else:
        result = divide(mtx, b//2)
        new_mtx = matrix_mul(result, result) # 짝수 제곱
        return new_mtx

mtx = [[1, 1],[1, 0]]
print(divide(mtx, n)[0][1])



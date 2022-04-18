# 행렬 곱셈을 활용한 피보나치 풀이
"""
(Fn+1 Fn  )  = (1 1)^n
(Fn   Fn-1)    (1 0)
"""
mod = 1000000
def matrix_mul(m1, m2):
    return [[sum(i*j for i,j in zip(row_a, column_b)) % mod for column_b in zip(*m2)] for row_a in m1]

def divide(matrix, n):
    if n == 1:
        return [[matrix[i][j] % mod for j in range(2)] for i in range(2)]
    elif n % 2: # 홀수
        return matrix_mul(matrix, divide(matrix, n-1)) # 이전에 짝수 제곱한 결과에 원래 matrix를 곱하면 홀수 제곱이 된다.
    else: # 짝수
        res = divide(matrix, n//2)
        return matrix_mul(res, res) # 짝수 제곱

print(divide([[1, 1], [1, 0]], int(input()))[0][1])
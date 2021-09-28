# def fac(n): # 재귀 오류 발생, sys.setrecursionlimit(100000000) 해주면 메모리 초과 발생
#     if n == 1:
#         return 1
#     return n * fac(n-1)

def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
n, k = map(int, input().split())
print(fac(n) // (fac(k) * fac(n - k)))
# 일반함수 -> O(n)
def fibo(n):
    a, b = 1, 1
    if n in [1, 2]:
        return 1
    for i in range(1, n):
        a, b = b, a+b
    return a
print(fibo(int(input())))

# 재귀함수 -> O(2^n)
def fibo(n):
    if n in [1, 2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(int(input())))

# DP -> O(n)
n = int(input())
fibo = [0 for _ in range(n+1)]
fibo[1] = 1
for i in range(2, n+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
print(fibo[n])

# 람다1 -> 재귀 함수 단순화 -> O(2^n)
fibo = lambda x: 1 if x <= 2 else fibo(x-1) + fibo(x-2)
print(fibo(int(input())))

# 람다2
fibo = lambda x, a=0, b=1: a if x <= 0 else fibo(x-1, b, a+b)
print(fibo(int(input())))
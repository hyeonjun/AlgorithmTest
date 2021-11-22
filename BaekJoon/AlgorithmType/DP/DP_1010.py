# 조합
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(factorial(b)//(factorial(b-a) * factorial(a)))

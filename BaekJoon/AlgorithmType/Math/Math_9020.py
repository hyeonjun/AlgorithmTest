# 소수 판별, 1100ms
def prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    x = n // 2
    for i in range(x, n):
        if prime(n-i) and prime(i):
            print(n-i, i)
            break

# 에라토스테네스의 체, 588ms
p = [True for _ in range(10001)]
for i in range(2, int(10000 ** 0.5) +1):
    if p[i]:
        for j in range(i*2, 10001, i):
            p[j] = False

for _ in range(int(input())):
    n = int(input())
    x = n // 2
    for i in range(x, n):
        if p[n-i] and p[i]:
            print(n-i, i)
            break
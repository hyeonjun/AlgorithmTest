"""
b^(X-2) = b^(-1)(mod X)

ex) X = 1000000007
 => b^(1000000005) = (a * b^(-1)) mod 1000000007

"""
MOD = 1000000007
def power(base, exp):
    if exp == 1:
        return base
    if exp % 2 == 0:
        result = power(base, exp//2)
        return (result * result) % MOD
    else:
        return (base * power(base, exp-1)) % MOD

def gcd(n, m): # n > m
    return n if m == 0 else gcd(m, n%m)

def inverse(n, s):
    return s * power(n, MOD-2) % MOD

m = int(input())
sum = 0
for _ in range(m):
    a, b = map(int, input().split())
    gcdV = gcd(a if a > b else b, b if a > b else a)
    a //= gcdV
    b //= gcdV # 기약분수로 만들기 위해서는 최대공약수로 분모와 분자를 약분하여야함
    sum += inverse(a, b)
    sum %= MOD
print(sum)



n, m = map(int, input().split(':'))

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

g = gcd(n, m) if n > m else gcd(m, n)
print(f'{n//g}:{m//g}')
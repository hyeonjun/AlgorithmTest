def gcd(n, m):
    return n if m == 0 else gcd(m, n%m)

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    g = gcd(a, b)
    print(a*b//g, g)
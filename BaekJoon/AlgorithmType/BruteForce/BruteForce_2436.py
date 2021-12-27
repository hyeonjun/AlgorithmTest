g, l = map(int, input().split())
n = l // g
a, b = 1, n

def gcd(a, b):
    return a if not b else gcd(b, a%b)

for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        c, d = i, n // i
        if gcd(c, d) == 1 and a+b > c+d:
            a, b = c, d
print(a*g, b*g)
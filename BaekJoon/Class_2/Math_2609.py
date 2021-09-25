a, b = map(int, input().split())
def gcd(n, m): # n이 더 커야함
    return n if m == 0 else gcd(m, n%m)
gcd_n = gcd(a, b) if a > b else gcd(b, a)
lcm_n = a * b // gcd_n
print(gcd_n) # 최대공약수
print(lcm_n) # 최소공배수
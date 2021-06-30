def solution(n, m):
    answer = []
    def gcd(n,m):
        while m > 0:
            n, m = m, n%m
        return n
    if m>n:
        n,m = m,n
    gN = gcd(n,m)
    answer.append(gN)
    answer.append(n * m // gN)
    return answer

print(solution(3, 12))
print(solution(2, 5))

def solution(n, m):
    def gcd(n, m):
        return n if m==0 else gcd(m, n%m)
    gn = gcd(n, m) if n > m else gcd(m, n)
    lcd = n*m // gn
    return [gn, lcd]

print(solution(3, 12))
print(solution(2, 5))
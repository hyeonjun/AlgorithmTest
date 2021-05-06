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
"""
카탈란 수
C1 = C0C0
C2 = C0C1 + C1C0
C3 = C0C2 + C1C1 + C2C0
C4 = C0C3 + C1C2 + C2C1 + C3C0
...

=> Cn = (2n)! // ((n+1)! * n!)
"""
def solution(n):
    def fct(n):
        if n == 1:
            return 1
        return n * fct(n - 1)
    return fct(2 * n) // (fct(n) * fct(n + 1))

print(solution(2)) # 2
print(solution(3)) # 5
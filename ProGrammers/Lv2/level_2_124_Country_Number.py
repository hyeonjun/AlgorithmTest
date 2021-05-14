def solution(n):
    T = "124"
    q, r = divmod(n-1, 3)
    return T[n-1] if n <= 3 else solution(q) + T[r]


# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
print(solution(5))

def solution(n):
    T = "412"
    return '' if n == 0 else solution((n-1)//3) + T[n%3]

print(solution(5))
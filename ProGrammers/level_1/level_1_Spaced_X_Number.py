def solution(x, n):
    return [i * x + x for i in range(n)]

print(solution(2, 5))
print(solution(-4, 2))
print(solution(0, 2))

def solution(x, n):
    if x == 0:
        return [0] * n
    return [i for i in range(x, x*n+1, x)] if x > 0 else sorted([i for i in range(x*n, x+1, -x)], reverse=True)

print(solution(2, 5))
print(solution(-4, 2))
print(solution(0, 2))
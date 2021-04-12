def solution(A):
    A = sorted(A)
    a = A[-1] * A[-2] * A[-3]
    b = A[0] * A[1] * A[-1]

    return a if a>b else b

print(solution([-5,5,-5,4]))

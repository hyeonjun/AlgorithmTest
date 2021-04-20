def solution(A, B):
    """
    1 - 1
    2 - 11 2 2
    3 - 111 12 21 3
    4 - 1111 112 121 211 22 5
    5 - 8
    1 2 3 5 8 13 .. => 피보나치
    """
    N = len(A)
    max_modulo = 2 ** 30
    fibo = [0,1,2]
    for i in range(2,len(A)):
        fibo.append((fibo[i]+fibo[i-1]) % max_modulo)

    result = [0] * N
    for i in range(N):
        result[i] = fibo[A[i]] % (2 ** B[i])
    return result
    pass

print(solution([4,4,5,5,1],[3,2,4,3,1]))


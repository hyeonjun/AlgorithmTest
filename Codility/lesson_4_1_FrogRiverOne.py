def solution(X, A):
    position_check = [0] * (X+1)
    exit = 0

    for i in range(len(A)):
        if position_check[A[i]] == 0:
            position_check[A[i]] = 1
            exit += 1

            if exit == X:
                return i
    return -1

X = 5
A = [1,1,1,1]
B = [1,3,1,4,2,3,5,4]
print(solution(X, A))
print(solution(X, B))
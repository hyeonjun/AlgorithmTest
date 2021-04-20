def solution(A):
    # 출발점과 도달점 추가
    A = [1] + A + [1] # [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1]
    N = len(A) # 13
    fibo = [1,1] # [1, 1, 2, 3, 5, 8]
    while fibo[-1] + fibo[-2] < N:
        fibo.append(fibo[-1] + fibo[-2])

    B = [-1] * N
    B[0] = 0 # [0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

    for i in range(N):
        if B[i] != -1:
            for f in fibo:
                target = f + i
                if target >= N:
                    break
                if A[target] == 1:
                    if B[target] == -1:
                        B[target] = B[i] + 1
                    elif B[target] > B[i] + 1:
                        B[target] = B[i] +1
    print(B)
    return B[-1]


print(solution([0,0,0,1,1,0,1,0,0,0,0]))
print(solution([1,1]))
print(solution([0,0,0,0,0,0,0,0,0,0,0,0,0]))
print(solution([1,1,0,0,0]))


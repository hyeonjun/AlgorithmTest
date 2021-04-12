def solution(A): # 100%
    check =  [0]*(len(A)+1)

    for i in range(1,len(A)+1):
        if A[i-1] <= len(A):
            check[A[i-1]-1] =1

    for i in range(1, len(A)+1):
        if check[i-1] == 0: return 0
    return 1

print(solution([4,1,2,3]))
print(solution([4,1,3]))
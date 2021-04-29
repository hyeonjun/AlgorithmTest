def solution(A):
    N = len(A)
    result = [A[0]] * (N+6)
    for i in range(1,N):
        result[i+6] = max(result[i:i+6])+A[i]
    return result[-1]

print(solution([1,-2,0,9,-1,-2]))
print(solution([1,1,1,1,1,1,1,1,1,1,1]))
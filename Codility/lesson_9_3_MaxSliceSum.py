def solution(A):
    check = 0
    if A[0]>0:
        check=A[0]
    maxSum = A[0]
    for i in A[1:]:
        sValue = check + i
        maxSum = max(maxSum, sValue)
        check = max(0, sValue)
    return maxSum


print(solution([3,2,-6,6,0]))
print(solution([3,2,-6,4,0]))
print(solution([-2,1]))
def solution(A):
    if len(A) < 2:
        return 0
    result = 0
    bValue = A[0]
    current = 0
    for i in A[1:]:
        if i > bValue:
            current = i - bValue
        else:
            bValue = i
        result = max(result, current)
    return result
    pass


print(solution([23171,21011,21123,21366,21013,21367]))
print(solution([5,4,3,2,1]))
print(solution([1,2,3,4,5]))
print(solution([8,9,3,6,1,2]))
print(solution([0,20000]))
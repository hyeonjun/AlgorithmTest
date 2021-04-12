def solution(A):
    if len(A) == 0:
        return 0

    result = set(A)
    return len(result)

print(solution([2,1,1,2,3,1]))
def solution(A):
    N = len(A)
    Abslist = []
    for i in range(N):
        value = abs(A[i])
        Abslist.append(value)

    return len(set(Abslist))

print(solution([-5,-3,-1,0,3,6]))
print(solution([1,1]))
print(solution([-2147483648, 0]))
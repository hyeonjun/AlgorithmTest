def solution(A):
    if len(A) == 0:
        return 1
    else:
        A = sorted(A)
        for i in range(len(A)):
            if i != (A[i]-1):
                return i+1
        # mn = min(A)
        # mx = max(A)
        # for i in range(mn,mx+1):
        #     if(i not in A):
        #         return i
    return A[-1]+1

A = [1]
B = []
C = [2,1,5,3,6,8,9,7]
print(solution(A))
print(solution(B))
print(solution(C))

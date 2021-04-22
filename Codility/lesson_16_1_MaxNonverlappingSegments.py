def solution(A,B):
    N = len(A)
    if N<2:
        return N
    count = 1
    end_point = B[0]
    for i in range(1,N):
        if A[i]>end_point:
            count+=1
            end_point = B[i]
    pass
print(solution([1,3,7,9,9],[5,6,8,9,10]))

"""
- A[I] ≤ B[I], for each I (0 ≤ I < N)
- B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1)

1 2 3 4 5 6 7 8 9 10
---------
    -------
            ---
                -
                ----
"""
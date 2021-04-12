def solution(A): # 내 힘으로 못풀었음.
    N = len(A)
    left = [0]*N
    right = [0]*N

    for i in range(1, N-2):
        left[i] = max(left[i-1]+A[i],0)

    for i in range(N-2,1,-1):
        right[i] = max(right[i+1]+A[i],0) # -1로 시작하지 않도록 방지

    max_slice_sum = left[0] + right[2]
    for i in range(1,N-1):
        max_slice_sum = max(max_slice_sum, left[i-1]+right[i+1])

    return max_slice_sum
print(solution([3,2,6,-1,4,5,-1,2]))
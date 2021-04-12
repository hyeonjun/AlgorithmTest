def solution(A):
    N = len(A)
    if N < 3:
        return 0

    peaks = []
    for i in range(1,len(A)-1):
        if A[i-1] < A[i] and A[i+1] < A[i]:
            peaks.append(i)

    if len(peaks) < 3:
        return len(peaks)

    # 최대한 깃발을 꽂을 수 있는 개수
    import math
    maxflag = int(math.sqrt(peaks[-1]-peaks[0]))+1

    for i in range(maxflag,2,-1):
        count = 1
        p = peaks[0]
        for pe in peaks:
            if i <= pe-p:
                count+=1
                p = pe
        if count >= i:
            break
    return i

print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))
# print(solution([1,3,2]))
# print(solution([0]))
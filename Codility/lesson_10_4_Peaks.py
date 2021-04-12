def solution(A):
    N = len(A) # 12
    if N < 3:
        return 0

    peaks = [] # [3, 5, 10]

    for i in range(1,N-1):
        if A[i-1]<A[i]>A[i+1]:
            peaks.append(i)

    peakCount = len(peaks)
    if peakCount == 0:
        return 0
    elif peakCount == 1:
        return 1
    # print(peaks) # [1, 3, 5, 7, 9]
    for i in range(peakCount, 0, -1): # 5, 4, 3, 2, 1
        if N%i == 0:
            count = 0
            size = N//i
            block = [0]*i
            for j in range(peakCount): # 0, 1, 2, 3, 4 * 4
                idx = peaks[j] // size
                if block[idx] == 0:
                    block[idx] = 1
                    count+= 1
            if count == i:
                return i





print(solution([1,2,3,4,3,4,1,2,3,4,6,2]))
print(solution([0,1,0,1,0,1,0,1,0,1,0,1]))
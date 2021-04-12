def solution(A):
    checker = (A[0]+A[1])/2
    checkIndex = 0
    for i in range(2, len(A)):
        avg = (A[i-2]+A[i-1]+A[i])/3.0
        if(checker > avg):
            checker = avg
            checkIndex = (i-2)
        avg = (A[i-1]+A[i])/2.0
        if(checker > avg):
            checker = avg
            checkIndex = (i-1)
    return checkIndex

print(solution( [-3, -5, -8, -4, -10]))
def solution(A, B):
    if len(A) == 1:
        return 1

    checker = []
    for a, b in zip(A,B):
        checker.append([a,b])
    result = []
    result.append(checker[0])
    for i in range(1, len(checker)):
        while(True):
            if result[-1][1] == 1 and checker[i][1] == 0:
                if result[-1][0] > checker[i][0]:
                    break
                else:
                    del result[-1]
                    if len(result) == 0:
                        result.append(checker[i])
                        break
            else:
                result.append(checker[i])
                break
    return len(result)


def MySolution(A, B): # 50%
    try:
        for i in range(len(A)):
            if (B[i] == 1) and (B[i + 1] == 0):
                if A[i] < A[i + 1]:
                    del A[i]
                    del B[i]
                    solution(A, B)
                else:
                    del A[i + 1]
                    del B[i + 1]
                    solution(A, B)
    except:
        return len(A)

# 0은 상류 1은 하류

print(solution([4,3,2,1,5],[0,1,0,0,0]))
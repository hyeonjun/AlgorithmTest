##############################################################################
# Lesson 2 - CyclicRotation
##############################################################################
def Solution1(A, K):
    if(len(A) > 0):
        loc = len(A)
        if(K > 0):
            for _ in range(K):
                temp = A[loc-1]
                del A[loc-1] # 삭제
                A.insert(0,temp)
                # print(A)
    return A
#
print(Solution1([3, 8, 9, 7, 6], 3))
print(Solution1([1, 2, 3, 4], 4))
print(Solution1([0,0,0],3))
print(Solution1([],0))

def Solution2(A, K):
    result = []
    # 0 1 2 3 4 시작
    # 4 0 1 2 3
    # 3 4 0 1 2
    # 2 3 4 0 1 결과
    # K = 3
    # i = 0 1 2 3 4
    # 0 -> 3, 1 -> 4, 2 -> 0, 3 -> 1, 4 -> 2
    for i in range(len(A)):
        result.insert((i+K)%len(A), A[i])
    return result

print(Solution2([3, 8, 9, 7, 6], 3))
print(Solution2([1, 2, 3, 4], 4))
print(Solution2([0,0,0],3))
print(Solution2([],0))
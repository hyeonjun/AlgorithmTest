# def FirstSolution(A): # 63% O(N ** 3)
#     N = len(A)
#     A.sort()
#
#     count = 0
#     for i in range(N):
#         for j in range(i+1, N):
#             q = j +1
#             while q < N:
#                 if A[i] + A[j] > A[q] and A[j] + A[q] > A[i] and A[q] + A[i] > A[j]:
#                     count += 1
#                 q += 1
#     return count
#     pass
#
# print(FirstSolution([10,2,5,1,8,12]))

def solution(A):
    A.sort()
    N = len(A)
    count = 0
    for i in range(0, N-2):
        j = i + 1
        k = i + 2
        while k < N:
            if A[i] + A[j] > A[k]:
                print(i,j,k)
                count += k - j
                k += 1
            elif j < k - 1:
                j += 1
            else:
                j+=1
                k+=1
    return count
    pass
# 0 1 2 3 4  5
# 1 2 5 8 10 12  234 345 | 235 ~ 245
print(solution([10,2,5,1,8,12]))



















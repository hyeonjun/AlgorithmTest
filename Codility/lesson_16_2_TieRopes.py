# def solution(K,A):
#     N = len(A)
#     check = [0] * (N+1)
#     count = 0
#     for i in range(N):
#         if check[i] >= K:
#             check[i+1] = A[i]
#         else:
#             check[i+1] = check[i] + A[i]
#     for i in check:
#         if i >= K:
#             count+=1
#     return count
# print(solution(4, [1,2,3,4,1,1,3]))

def SideSolution(K,A):
    count = 0

    tmp = 0
    for i in A:
        tmp += i
        if tmp >= K:
            count +=1
            tmp = 0
    return count
print(SideSolution(4, [1,2,3,4,1,1,3]))


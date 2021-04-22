# def firstSolution(A): # 45% O(N*N)
#     A = list(set(A))
#     N = len(A)
#     for i in range(len(A)-1, 0, -1):
#         N += i
#     check = [0] * N
#     ckIdx = 0
#     for i in range(len(A)):
#         for j in range(i,len(A)):
#             check[ckIdx] = abs(A[i]+A[j])
#             ckIdx+=1
#     return min(check)
#     pass
# print(firstSolution([1,4,-3,2,-5]))

def SecondeSolution(A):
    A = list(sorted(set(A))) # -5 -3 1 2 4
    print(A)
    N = len(A)
    first = 0
    last = N-1
    result = abs(A[0] + A[-1])
    while first <= last:
        tmp = A[first] + A[last]
        print(first, last, tmp)
        result = min(result, abs(tmp))
        if tmp <= 0:
            first+=1
        else:
            last-=1
    return result

print(SecondeSolution([1,4,-5,7,9,-1,-3,10]))
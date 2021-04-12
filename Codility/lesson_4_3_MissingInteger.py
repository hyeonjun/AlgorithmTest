def MySolution(A): # 66%
    for i in range(1, len(A)+1):
        if i not in A:
            return i
    return len(A)+1
# print(MySolution([1,3,6,4,1,2]))
# print(MySolution([1,2,3]))
# print(MySolution([-1,-3]))

def solution(A): # 100%
    check = [0] * (len(A)+1)
    checkCount = 0
    for i in range(1, len(A)+1):
        if (A[i-1] > 0) and (A[i-1] < len(A)+1):
            check[A[i-1]-1] = 1

    for i in range(1,len(check)+1):
        if check[i-1] == 0: return i
        else: checkCount+=1
    return checkCount+1

print(solution([1,3,6,4,1,2]))
print(solution([1,2,3]))
print(solution([-1,-3]))
print(solution([2]))
print(solution([4, 5, 6, 2]))
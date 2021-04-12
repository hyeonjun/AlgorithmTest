def solution(A): # 50% || time out(O(N^2))
    checker = []
    for i in range(len(A)):
        value=0
        for j in range(len(A)):
            if i == j:
                pass
            if (((-A[i]+i)<(-A[j]+j)) and ((-A[j]+j)<=(A[i]+i)) or
                (((-A[i]+i)<=(A[j]+j)) and ((A[j]+j)<(A[i]+i)))):
                if([i if i<j else j,j if j>i else i] not in checker):
                    checker.append([i if i<j else j,j if j>i else i])
                    value+=1
                    if value>10000000 :
                        return -1
    return len(checker)
# print(solution([1,1,1]))

def SideSolution(A):
    check = []
    for i,v in enumerate(A):
        check.append((i-v, -1))
        check.append((i+v, 1))
    check.sort()
    intersections = 0
    intervals = 0
    for i, v in enumerate(check):
        if v[1] == 1:
            intervals -= 1
        if v[1] == -1:
            intersections += intervals
            intervals += 1
    return -1 if intersections>10000000 else intersections
print(SideSolution([1,5,2,1,4,0]))
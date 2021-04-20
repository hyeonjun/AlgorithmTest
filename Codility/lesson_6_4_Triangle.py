def solution(A):
    check = []
    for i in A:
        if(i>0):
            check.append(i)
    check.sort() # [1, 2, 5, 8, 10, 20]
    for i in range(len(check) - 1, -1, -1):
        for j in range(0, i-1):
            if (((check[i-1]+check[j]) > check[i]) and ((check[j] + check[i]) > check[i-1]) and ((check[i] +check[i-1]) > check[j])):
                return 1
    return 0
print(solution([10,2,5,1,8,12]))
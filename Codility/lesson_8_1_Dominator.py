def solution(A):
    check = {}
    length = len(A)
    checker = 0

    if length == 0:
        return -1

    for i in A:
        if i not in check.keys():
            check[i] = 1
        else:
            check[i] += 1
    maxValue = max(check.values())
    if maxValue > length/2:
        for key, value in check.items():
            if maxValue == value:
                checker = key
        for i in range(length):
            if checker == A[i]:
                return i

    return -1


print(solution( [2, 1, 1, 3]))
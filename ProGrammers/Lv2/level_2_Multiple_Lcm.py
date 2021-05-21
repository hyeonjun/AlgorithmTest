def solution_1(arr):
    arr.sort(reverse=True)
    answer = arr[0]
    for n in arr[1:]:
        tmp1, tmp2 = answer, n
        while tmp2 > 0:
            tmp1, tmp2 = tmp2, tmp1%tmp2
        answer = answer * n // tmp1
    return answer

def solution_2(arr):
    from math import gcd
    answer = arr[0]
    for n in arr:
        answer = answer*n // gcd(answer, n)
    return answer

data = [[2,6,8,14], [1,2,3]] # 168, 6
for i in data:
    print(solution_1(i))
    print(solution_2(i))

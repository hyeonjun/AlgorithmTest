# -*- coding:cp949 -*-
def solution(n, k):
    from math import factorial as fc
    answer = []
    num_list = list(range(1, n + 1))
    while n != 0:
        fact = fc(n - 1)
        idx, k = (k - 1) // fact, k % fact
        answer.append(num_list.pop(idx))
        n -= 1
    return answer

print(solution(3, 5))

def solution(n, k): # 시간 초과
    from itertools import permutations
    return list(permutations(range(1,n+1), n))[k-1]

print(solution(3, 5))
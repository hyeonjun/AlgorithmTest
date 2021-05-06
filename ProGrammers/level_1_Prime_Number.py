from itertools import combinations
import math
def solution(nums):
    def check(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0: return False
        return True

    answer = 0
    for i in combinations(nums, 3):
        sumN = sum(i)
        if check(sumN):
            answer+=1

    return answer

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
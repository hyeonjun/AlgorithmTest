def solution(numbers):
    answer = []
    from itertools import combinations
    for i in combinations(numbers, 2):
        sumN = sum(i)
        if sumN not in answer:
            answer.append(sumN)

    answer.sort()
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
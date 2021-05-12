def solution(numbers):
    answer = []
    from itertools import combinations
    for i in combinations(numbers, 2):
        for j in zip(*i):
            print(j)
        print()
            # sumN = sum(i)

        # if sumN not in answer:
        #     answer.append(sumN)

    # answer.sort()
    return 0

print(solution([[2,1],[1,2],[3,3],[4,4],[1,5]]))
# print(solution([5,0,2,7]))
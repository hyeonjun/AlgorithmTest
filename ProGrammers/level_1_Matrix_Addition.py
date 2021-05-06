def solution(arr1, arr2):
    return [[sum(row) for row in zip(*t)] for t in zip(arr1, arr2)]

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
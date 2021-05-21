def solution(arr1, arr2):
    return [[sum(a*b for a,b in zip(row_a, col_b)) for col_b in zip(*arr2)] for row_a in arr1]
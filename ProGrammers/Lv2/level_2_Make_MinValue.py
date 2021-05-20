def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    tmp = list(map(lambda x, y: x * y, A, B))

    return sum(tmp)

print(solution([1,4,2], [5,4,4])) # 29
print(solution([1,2], [3,4])) # 10
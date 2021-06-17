def solution(works, n): # max를 사용하면 효율성에 문제 발생
    if sum(works) <= n:
        return 0
    for i in range(n):
        maxV = max(works)
        idx = works.index(maxV)
        works[idx] -= 1

    return sum([i ** 2 for i in works])

print(solution([4,3,3], 4)) # 12
print(solution([2,1,2], 1)) # 6
print(solution([1,1], 3)) # 0

def solution(works, n): # 최대 힙
    if sum(works) <= n:
        return 0

    import heapq
    work = []
    for i in works:
        heapq.heappush(work, (-i,i))

    for i in range(n):
        w = heapq.heappop(work)[1] - 1
        heapq.heappush(work, (-w, w))

    return sum([w[1] ** 2 for w in work])

print(solution([4,3,3], 4)) # 12
print(solution([2,1,2], 1)) # 6
print(solution([1,1], 3)) # 0
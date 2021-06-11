# -*- coding:utf-8 -*-
# 최소 힙
def solution(array):
    import heapq
    answer = []
    heap = []
    for i in array:
        if i != 0:
            heapq.heappush(heap, i)
        else:
            if len(heap) == 0:
                answer.append(0)
            else:
                answer.append(heapq.heappop(heap))
    return answer

print(solution([0,12345678,1,2,0,0,0,0,32])) # [0, 1, 2, 12345678, 0]
# =============================================================================

# 카드 정렬하기
def solution(cards):
    import heapq
    heap = []
    for i in cards:
        heapq.heappush(heap, i)

    answer = 0
    while len(heap) != 1:
        sumV = heapq.heappop(heap) + heapq.heappop(heap)
        answer += sumV
        heapq.heappush(heap, sumV)
    return answer

print(solution([10,20,40]))
print(solution([7,1,2,3]))
# =============================================================================

# 문제집
def solution(n,m,problem): # 위상 정렬
    import heapq
    indegree = [0] * (n+1) # 진입 차수
    array = [[] for _ in range(n+1)]
    for x,y in problem:
        array[x].append(y)
        indegree[y]+=1

    heap = []
    result = []

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            heapq.heappush(heap, i)

    while heap:
        data = heapq.heappop(heap)
        result.append(data)
        for i in array[data]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(heap, i)

    return result

print(solution(4,2,[[4,2],[3,1]]))
print(solution(7,2, [[7,5],[5,3]]))
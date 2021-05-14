def solution(scoville, K):
    import heapq
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            count += 1
        except:
            return -1
    return count
print(solution([1,2,3,9,10,12], 7))
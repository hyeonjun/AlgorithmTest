def solution(food_times, k):
    import heapq

    n = len(food_times)
    pre = 0  # 이전에 제거한 음식의 food_time
    heap = []
    for i in range(n):
        heapq.heappush(heap, (food_times[i], i + 1))  # (음식양, 번호)

    while heap:
        # 먹는데 걸리는 시간: 남은 양 * 남은 음식 개수
        # 시간이 가장 적게 걸리는 음식을 가져옴
        time = (heap[0][0] - pre) * n
        if k >= time:
            k -= time
            pre, _ = heapq.heappop(heap)
            n -= 1
        # 시간 부족시
        else:
            idx = k % n
            heap.sort(key=lambda x: x[1])
            return heap[idx][1]
    return -1

print(solution([3,1,2], 5)) # 1
def solution(jobs):
    answer, time, i, now = 0, -1, 0, 0
    import heapq
    heap = []
    while i < len(jobs):
        for x, y in jobs:
            if time < x <= now:
                heapq.heappush(heap, [y, x])
        if len(heap) > 0:
            job = heapq.heappop(heap)
            time = now
            now += job[0]
            answer += now - job[1]
            i += 1
        else:
            now += 1

    return answer // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]])) # 9
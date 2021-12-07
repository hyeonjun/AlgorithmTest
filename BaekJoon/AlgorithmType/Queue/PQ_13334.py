import heapq
n = int(input())
arr = [sorted(list(map(int, input().split()))) for _ in range(n)]
arr.sort(key=lambda x: x[1])
d = int(input())
heap = []
answer = 0
for s, e in arr:
    if e-s > d:
        continue
    heapq.heappush(heap, s)
    while heap and heap[0] < e-d: # 현재 철로 안에 들어오지 않는 것들 전부 pop
        heapq.heappop(heap)
    answer = max(answer, len(heap))
print(answer)
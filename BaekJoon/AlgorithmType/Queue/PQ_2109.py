import heapq
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x:x[1])
heap = []
for i in lst:
    heapq.heappush(heap, i[0])
    if len(heap) > i[1]:
        heapq.heappop(heap)
print(sum(heap))
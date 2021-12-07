import heapq
n = int(input())
heap = []
days = [0 for _ in range(1001)]
for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(heap, (-w, d)) # 최대힙

while heap:
    data = heapq.heappop(heap)
    for i in range(data[1], 0, -1):
        if days[i] == 0:
            days[i] = -data[0]
            break
print(sum(days))

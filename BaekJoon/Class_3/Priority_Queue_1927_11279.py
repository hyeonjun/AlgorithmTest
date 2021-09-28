# 1927 최소 힙
import heapq
import sys
heap = []
for _ in range(int(input())):
    d = int(sys.stdin.readline())
    if d == 0:
        print(heapq.heappop(heap) if heap else 0)
    else:
        heapq.heappush(heap, d)

# 11279 최대 힙
import heapq
import sys
heap = []
for _ in range(int(input())):
    d = int(sys.stdin.readline())
    if d == 0:
        print(heapq.heappop(heap) * -1 if heap else 0)
    else:
        heapq.heappush(heap, -d)
import heapq, sys
# 0이면 절대값이 작은 수 출력
# 0이 아니면 삽입
heap = []
for _ in range(int(input())):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        print(heapq.heappop(heap)[1]) if len(heap) > 0 else print(0)
    else:
        heapq.heappush(heap, (x if x > 0 else -x, x))

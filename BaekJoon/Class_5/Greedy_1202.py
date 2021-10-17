import heapq, sys
input = sys.stdin.readline
n, k = map(int, input().split())
jewel = []
for _ in range(n):
    w, v = map(int, input().split())
    heapq.heappush(jewel, [w, v])
bag = []
for _ in range(k):
    c = int(input())
    heapq.heappush(bag, c)

answer = 0
tmp = []
for _ in range(k):
    c = heapq.heappop(bag) # 현재 수용량
    while jewel and c >= jewel[0][0]:
        heapq.heappush(tmp, -heapq.heappop(jewel)[1]) # 가치에 대한 최대힙
    if tmp:
        answer -= heapq.heappop(tmp)
print(answer)



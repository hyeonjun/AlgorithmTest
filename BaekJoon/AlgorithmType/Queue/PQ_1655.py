import heapq
import sys
input = sys.stdin.readline
n = int(input())
left, right = [], []
for _ in range(n):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        l, r = heapq.heappop(left), heapq.heappop(right)
        heapq.heappush(left, -r)
        heapq.heappush(right, -l)
    print(-left[0])

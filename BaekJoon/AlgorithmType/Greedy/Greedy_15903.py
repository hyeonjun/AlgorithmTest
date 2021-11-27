import sys
input = sys.stdin.readline

# sort =====================================
# n, m = map(int, input().split())
# card = list(map(int, input().split()))
# for i in range(m):
#     card.sort()
#     newN = card[0] + card[1]
#     card[0], card[1] = newN, newN
# print(sum(card))

# heapq =====================================
import heapq
n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

for i in range(m):
    x, y = heapq.heappop(card), heapq.heappop(card)
    heapq.heappush(card, x+y)
    heapq.heappush(card, x+y)
print(sum(card))
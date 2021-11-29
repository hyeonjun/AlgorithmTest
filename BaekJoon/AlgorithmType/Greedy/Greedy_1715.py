import heapq
n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)

if len(card) == 1:
    print(0)
else:
    answer = 0
    while len(card) > 1:
        a, b = heapq.heappop(card), heapq.heappop(card)
        answer += a+b
        heapq.heappush(card, a+b)
    print(answer)
import heapq
k, n = map(int, input().split())
prime = list(map(int, input().split()))
heap = [1]
answer = 0
for _ in range(n+1):
    answer = heapq.heappop(heap) # n번째 수
    for i in range(k):
        heapq.heappush(heap, prime[i] * answer)
        print(answer, prime[i])
        if answer % prime[i] == 0: # 약수 - 12의 경우 4*3 6*2가 나올 수 있는데
            print(heap, answer, prime[i])
            break
print(answer)

# 실패, 메모리 초과
# import heapq
# k, n = map(int, input().split())
# prime = list(map(int, input().split()))
# heap = [1]
# visited = {}
# answer = 0
# for _ in range(n+1):
#     answer = heapq.heappop(heap) # n번째 수
#     for i in range(k):
#         value = prime[i] * answer
#         if visited.get(value):
#             continue
#         heapq.heappush(heap, value)
#         visited[value] = 1
# print(answer)
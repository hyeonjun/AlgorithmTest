"""
수가 들어올 때마다 정렬하면서 중앙값을 구하면 시간초과난다.
min_heap과 max_heap을 사용하여 중앙값을 구한다.

"""
import heapq

def midValue(num):
    min_heap, max_heap = [], []
    mid = num[0]
    answer = [mid]
    for i, v in enumerate(num[1:], 1):
        if v > mid:
            heapq.heappush(max_heap, v)
        else:
            heapq.heappush(min_heap, -v)

        if i % 2 == 0: # 홀수번째
            if len(min_heap) < len(max_heap): # 길이가 다르면 맞춰야함
                heapq.heappush(min_heap, -mid)
                mid = heapq.heappop(max_heap)
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, mid)
                mid = -heapq.heappop(min_heap)
            answer.append(mid)
    print(len(answer))
    for i in range(len(answer)):
        if i !=0 and (i+1) % 10 == 1:
            print()
        print(answer[i], end=' ')
    print()

for _ in range(int(input())):
    m = int(input())
    num = []

    if m % 10 == 0:
        for _ in range(m//10):
            num.extend(list(map(int, input().split())))
    else:
        for _ in range(m//10+1):
            num.extend(list(map(int, input().split())))
    midValue(num)
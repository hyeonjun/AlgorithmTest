# 센서
def solution(n,k,censor):
    if k >= n:
        return 0
    censor.sort()
    distances = [censor[i]-censor[i-1] for i in range(1,n)]
    distances.sort(reverse=True)
    for _ in range(k-1):
        distances.pop(0)
    return sum(distances)

# print(solution(6,2,[1,6,9,3,6,7])) # 5
# =============================================================================

# 도서관
def solution(n,m,book):
    import heapq
    # 가장 먼 책
    farthest = max(max(book), -min(book))
    positive = []
    negative = []
    for i in book:
        if i > 0:
            heapq.heappush(positive, -i)
        else:
            heapq.heappush(negative, i)

    answer = 0
    while positive:
        answer += heapq.heappop(positive) # heappop은 가장 작은 원소부터 출력한다.
        for _ in range(m-1):
            if positive:
                heapq.heappop(positive)
    while negative:
        answer += heapq.heappop(negative)
        for _ in range(m-1):
            if negative:
                heapq.heappop(negative)
    return -answer * 2 - farthest

print(solution(7,2,[-37,2,-6,-39,-29,11,-28])) # 131
# ==============================================================================

# 컵라면
def solution(n, array):
    import heapq
    array.sort()
    queue = []
    for i in array:
        heapq.heappush(queue, i[1])
        if i[0] < len(queue):
            heapq.heappop(queue)
        print(queue)
    return sum(queue)
# n = int(input())
# array = []
# for i in range(n):
#     a, b = map(int, input().split(' '))
#     array.append([a,b])
# print(solution(n, array))

print(solution(7, [[1,6],[1,7],[3,2],[3,1],[2,4],[2,5],[6,1]]))
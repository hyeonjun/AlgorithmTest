def solution(citations):
    N = len(citations)
    citations.sort()
    for i in range(N):
        if N-i <= citations[i]:
            return N-i
    return 0

print(solution([3,0,6,1,5])) # 3
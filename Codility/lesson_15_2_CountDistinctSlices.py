def solution(M,A):
    appearance = [False] * (M + 1)
    N = len(A)
    front = 0
    slices = 0
    for back in range(N):
        while front < N and appearance[A[front]] == 0: # 시작점 위치 찾기
            appearance[A[front]] += 1 # 비교했는지 확인
            slices += front - back +1 # 갯수
            front += 1 # 비교 대상 위치 옮기기
        appearance[A[back]] -= 1 # 초기화
        if slices >= 1000000000: return 1000000000
    return slices
print(solution(6,[3,4,5,5,2]))
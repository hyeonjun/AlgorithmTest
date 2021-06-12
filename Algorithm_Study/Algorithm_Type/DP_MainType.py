# LCS
def solution(str1, str2):
    n, m = len(str1), len(str2)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

print(solution("ACAYKP", "CAPCAK"))
# =============================================================================

# 기타 리스트
def solution(N,S,M,V):
    dp = [[False] * (M+1) for _ in range(N+1)]
    dp[0][S] = True
    for i in range(1, N+1):
        for j in range(M+1):
            if dp[i-1][j] == True:
                if j - V[i-1] >= 0:
                    dp[i][j-V[i-1]] = True
                if j + V[i-1] <=M:
                    dp[i][j+V[i-1]] = True

    answer = -1
    for i in range(M, -1, -1):
        if dp[N][i] == True:
            answer = i
            break
    return answer

print(solution(3,5,10,[5,3,7])) # 10
# =============================================================================

# 가장 높은 탑 쌓기
def solution(N, brick):
    array = [(0,0,0,0)]
    # 인덱스 번호 추가
    for i in range(1, N+1):
        area, height, weight = brick[i-1]
        array.append((i, area, height, weight))

    # 무게 기준 정렬
    array.sort(key=lambda x:x[3])

    dp = [0] * (N+1)
    for i in range(1, N+1): # 1 2  3   4    5
        for j in range(i):  # 0 01 012 0123 01234
            if array[i][1] > array[j][1]: # 넓이 비교
                dp[i]=max(dp[i], dp[j]+array[i][2])

    # 역추적
    answer = []
    idx = N
    max_V = max(dp)
    while idx != 0:
        if max_V == dp[idx]:
            answer.append(array[idx][0]) # 벽돌 번호
            max_V -= array[idx][2]
        idx -= 1
    return [len(answer), answer[::-1]]

# 벽돌 => 밑면넓이, 높이, 무게
print(solution(5, [[25,3,4],[4,4,6],[9,2,3],[16,2,5],[1,5,2]]))
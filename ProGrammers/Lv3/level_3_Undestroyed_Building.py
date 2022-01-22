# 카카오 2022 블라인드 6번
def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])

    delta = [[0 for _ in range(m+2)] for _ in range(n+2)] # 변화량 누적합

    # 변화량 계산
    for t, r1, c1, r2, c2, d in skill:
        if t == 1: d *= -1
        delta[r1+1][c1+1] += d
        delta[r2+2][c2+2] += d
        delta[r1+1][c2+2] -= d
        delta[r2+2][c1+1] -= d

    # 누적합 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            delta[i][j] += delta[i-1][j] + delta[i][j-1] - delta[i-1][j-1]

    # 건물 파괴 여부 확인
    for i in range(n):
        for j in range(m):
            if board[i][j] + delta[i+1][j+1] > 0:
                answer += 1

    return answer

print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 1e9

def divide(x, y, d1, d2):
    calc = [0 for _ in range(5)]
    bound = [[0 for _ in range(n)] for _ in range(n)]
    # 5번 구역 경계선
    for i in range(d1+1):
        bound[x+i][y-i] = 5
        bound[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        bound[x+i][y+i] = 5
        bound[x+d1+i][y-d1+i] = 5
    # 경계선 안 구역은 5번 구역
    for i in range(x+1, x+d1+d2):
        flag = False
        for j in range(n):
            if bound[i][j] == 5: # 경계 시작과 끝
                flag = not flag
            if flag:
                bound[i][j] = 5
    # 구역별 인구 계산
    for r in range(n):
        for c in range(n):
            if r < x+d1 and c <= y and bound[r][c] == 0: # 1번 구역
                bound[r][c] = 1
                calc[0] += board[r][c]
            elif r <= x+d2 and y < c and bound[r][c] == 0: # 2번 구역
                bound[r][c] = 2
                calc[1] += board[r][c]
            elif x+d1 <= r and c < y-d1+d2 and bound[r][c] == 0: # 3번 구역
                bound[r][c] = 3
                calc[2] += board[r][c]
            elif x+d2 < r and y-d1+d2 <= c and bound[r][c] == 0: # 4번 구역
                bound[r][c] = 4
                calc[3] += board[r][c]
            else:
                calc[4] += board[r][c]
    return max(calc) - min(calc)

for x in range(n):
    for y in range(n):
        for d1 in range(n):
            for d2 in range(n):
                if 0 <= x < x + d1 + d2 < n and 0 <= y-d1 < y < y+d2 < n:
                    answer = min(answer, divide(x, y, d1, d2))
print(answer)
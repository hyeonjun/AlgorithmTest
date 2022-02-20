"""
이동이 끝난 뒤, 2개 이상의 파이어볼이 있는 칸
- 4개의 파이어볼로 나뉨
    1. 질량 = 질량의 합 // 5
    2. 속력 = 속력 합 // 파이어볼 개수
    3. 방향 = 모든 방향이 홀수이거나 짝수이면 => 0, 2, 4, 6 / 그렇지 않으면 1, 3, 5, 7
- 질량이 0인 파이어볼 소멸
"""
n, m, k = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
fireball = []
for i in range(m):
    r, c, m, s, d = map(int, input().split())
    fireball.append([r-1, c-1, m, s, d])
direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

for _ in range(k):
    while fireball:
        r, c, m, s, d = fireball.pop(0)
        nr = (r + s * direction[d][0]) % n
        nc = (c + s * direction[d][1]) % n
        board[nr][nc].append([m, s, d])

    for i in range(n):
        for j in range(n):
            if len(board[i][j]) > 1: # 2개 이상의 파이어볼
                sumM, sumS, odd, even, cnt = 0, 0, 0, 0, len(board[i][j])
                while board[i][j]:
                    m_, s_, d_ = board[i][j].pop(0)
                    sumM += m_
                    sumS += s_
                    if d_ % 2: odd+=1
                    else: even+=1
                if odd == cnt or even == cnt: # 모든 방향이 홀수이거나 짝수
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sumM // 5: # 질량 0이면 소멸
                    for d_ in nd:
                        fireball.append([i, j, sumM//5, sumS//cnt, d_])
            # 1개의 파이어볼
            elif len(board[i][j]) == 1:
                fireball.append([i, j] + board[i][j].pop())
print(sum([f[2] for f in fireball]))

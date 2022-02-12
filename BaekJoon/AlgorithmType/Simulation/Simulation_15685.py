"""
0 세대: 0
1 세대: 0 / 1(0+1)
2 세대: 0, 1 / 2(1+1), 1(0+1)
3 세대: 0, 1, 2, 1 / 2(1+1), 3(2+1), 2(1+1), 1(0+1)
=> 전 세대 들에 1을 더하고 뒤집어준 방향대로 간다.
"""
n = int(input())
board = [[0 for _ in range(101)] for _ in range(101)] # 100 * 100 격자
direction = [[0, 1], [-1, 0], [0, -1], [1, 0]]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    board[x][y] = 1

    # 방법 1
    # nxt, prev = [d], [d]
    # for _ in range(g+1): # g번 세대를 걸쳐서 드래곤 커브 확장
    #     for i in nxt:
    #         x += direction[i][0]
    #         y += direction[i][1]
    #         board[x][y] = 1
    #     nxt = [(p + 1) % 4 for p in prev][::-1]
    #     prev += nxt

    # 방법 2
    curve = [d]
    for _ in range(g):
        for i in range(len(curve)-1, -1, -1):
            curve.append((curve[i]+1) % 4)
    for i in curve:
        x += direction[i][0]
        y += direction[i][1]
        board[x][y] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            answer += 1
print(answer)

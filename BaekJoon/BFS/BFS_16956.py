"""
늑대가 양에 가지 못하도록 울타리를 설치
1. 울타리 최소개수를 묻는 문제가 아님 -> 걍 빈칸은 다 울타리 쳐버리면된다
2. 빈칸모두를 다 쳐도 늑대가 양한테 갈수있으면 0 출력
"""

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

direction = [(1,0), (-1,0), (0,1), (0,-1)]
for x in range(r):
    for y in range(c):
        if board[x][y] == 'W':
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'S':
                    print(0)
                    exit(0)
        elif board[x][y] == 'S':
            continue

        else:
            board[x][y] = 'D'
print(1)
for i in board:
    print("".join(i))
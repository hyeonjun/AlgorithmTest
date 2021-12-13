import sys
input = sys.stdin.readline
from collections import deque
r, c, n = map(int, input().split())
board = [list(input()) for _ in range(r)]
direction = [(1,0),(0,1),(-1,0),(0,-1)]

def check():
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                bombList.append((i, j))

def installBomb():
    for i in range(r):
        for j in range(c):
            board[i][j] = 'O'

def bomb():
    while bombList:
        x, y = bombList.popleft()
        board[x][y] = '.'
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'O':
                board[nx][ny] = '.'

n -= 1 # 아무것도 안함
while n:
    bombList = deque()
    check()
    installBomb()
    n -= 1
    if n == 0:
        break
    bomb()
    n -= 1

for i in range(r):
    for j in range(c):
        print(board[i][j], end='')
    print()
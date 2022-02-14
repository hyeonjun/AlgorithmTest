import sys
from collections import deque
input=sys.stdin.readline
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(x, y):
    visited = [[-1 for _ in range(w+2)] for _ in range(h+2)]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h+2 and 0 <= ny < w+2 and visited[nx][ny] == -1:
                if board[nx][ny] == '.' or board[nx][ny] == '$': # 문 안열어도 됨
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft([nx, ny]) # 문을 열지 않고 움직이는 것을 우선적으로 움직일 수 있도록 한다
                elif board[nx][ny] == '#': # 문 열기
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
    return visited

for _ in range(int(input())):
    h, w = map(int, input().split())
    board = [list('.'*(w+2))]
    prisoner = []
    for i in range(h):
        tmp = ['.']+list(input().strip())+['.']
        for j in range(w+2):
            if tmp[j] == '$':
                prisoner.append((i+1, j))
        board.append(tmp)
    board.append(list('.'*(w+2)))

    v1, v2 = bfs(prisoner[0][0], prisoner[0][1]), bfs(prisoner[1][0], prisoner[1][1]) # 두 죄수 탈출
    v3 = bfs(0, 0) # 상근이가 밖에서 안으로 문 열기
    answer = 1e9

    for i in range(h+2):
        for j in range(w+2):
            if v1[i][j] != -1 and v2[i][j] != -1 and v3[i][j] != -1:
                res = v1[i][j] + v2[i][j] + v3[i][j]
                if board[i][j] == '*':
                    continue
                if board[i][j] == '#':
                    res -= 2 # 한번 연 문은 열려있기 때문에 두 명이 연 횟수는 빼야함
                answer = min(answer, res)
    print(answer)

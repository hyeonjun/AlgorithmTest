# Mooyo Mooyo
import sys
sys.setrecursionlimit(100000)  # 재귀의 제한을 늘림
def solution(n, k, board):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs_count(x, y): # 같은 수 몇 개?
        count = 1
        visited[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= 10:
                continue
            if board[x][y] == board[nx][ny] and not visited[nx][ny]:
                count += dfs_count(nx, ny)
        return count

    def dfs_delete(x, y, v): # 같은 수 삭제
        delete[x][y] = True
        board[x][y] = '0'
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= 10:
                continue
            if board[nx][ny] == v and not delete[nx][ny]:
                dfs_delete(nx, ny, v)

    def down():
        for i in range(10):
            tmp = []
            for j in range(n):
                if board[j][i] != '0':
                    tmp.append(board[j][i])
            for j in range(n-len(tmp)):
                board[j][i] = '0'
            for j in range(n-len(tmp), n):
                board[j][i] = tmp.pop(0)

    while True:
        ck = False
        visited = [[False for _ in range(10)] for _ in range(n)]
        delete = [[False for _ in range(10)] for _ in range(n)]
        for i in range(n):
            for j in range(10):
                if board[i][j] == '0' or visited[i][j]:
                    continue
                cnt = dfs_count(i, j)
                if cnt >= k:
                    dfs_delete(i, j, board[i][j])
                    ck = True # 삭제할 게 있었다면
        if not ck:
            break
        down()
    return board

board = [
['0','0','0','0','0','0','0','0','0','0'],
['0','0','0','0','0','0','0','3','0','0'],
['0','0','5','4','0','0','0','3','0','0'],
['1','0','5','4','5','0','2','2','3','0'],
['2','2','1','1','1','2','2','2','2','0'],
['1','1','1','1','1','1','1','2','2','3']]
new_Board = solution(6, 3, board)
for i in new_Board:
    print(i)
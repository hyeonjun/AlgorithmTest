class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        n, m = len(board), len(board[0])
        direction = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        for x in range(n):
            for y in range(m):
                cnt = 0 # 살아있는 이웃 개수
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < m and abs(board[nx][ny]) == 1:
                        cnt += 1
                if board[x][y] == 1:
                    if cnt < 2 or cnt > 3: # 죽음
                        board[x][y] = -1
                else:
                    if cnt == 3:
                        board[x][y] = 2
        for x in range(n):
            for y in range(m):
                if board[x][y] == -1: board[x][y] = 0
                elif board[x][y] == 2: board[x][y] = 1
        return board
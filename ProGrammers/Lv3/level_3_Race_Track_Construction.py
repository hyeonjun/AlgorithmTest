def solution(board):
    def bfs(start):
        table = [[float('inf') for _ in range(len(board))] for _ in range(len(board))]
        table[0][0] = 0  # 출발 지점

        # 상 0 하 1 좌 2 우 3
        move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        queue = [start]

        while queue:
            x, y, cost, dirt = queue.pop(0)

            for idx, (dx, dy) in enumerate(move):
                new_cost = cost + 600 if idx != dirt else cost + 100  # 직선은 100원 코너는 500원
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0 and table[nx][ny] > new_cost:
                    table[nx][ny] = new_cost
                    queue.append((nx, ny, new_cost, idx))
        return table[-1][-1]

    # x,y,cost,진행방향
    return min(bfs((0, 0, 0, 1)), bfs((0, 0, 0, 3)))  # 처음에 갈 수 있는 방향은 하, 우 밖에 없음

print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 900
# 3800
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) # 2100
# 3200
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
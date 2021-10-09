def solution(game_board, table):
    answer = 0
    n = len(game_board)
    # 1. game_board의 빈 공간 좌표와 table의 블록 좌표값을 BFS or DFS로 찾아내고 찾아낸 좌표값들을 정렬
    def bfs(x, y, visited, board, check_point):
        queue = [[x, y]]
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        space = [[x,y]]
        visited[x][y] = True
        while queue:
            x, y = queue.pop(0)
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 > nx or nx >= n or 0 > ny or ny >= n:
                    continue
                if not visited[nx][ny] and board[nx][ny] == check_point:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    space.append([nx, ny])
        return sorted(space)

    def standard(board): # 블록과 빈공간들을 모두 0,0에서 시작하도록 만든다
        tmp = []
        minx, miny = n, n
        for i in board:
            minx, miny = min(minx, i[0]), min(miny, i[1])
        for x, y in board:
            tmp.append([x-minx, y-miny])
        return sorted(tmp)

    def rotate(board):
        tmp = []
        for b in board:
            tmp.append([b[1], n-1-b[0]])
        return standard(tmp)


    # game_board = 0
    # table = 1
    game_board_empty, table_block = [], []
    visited_game, visited_table = [[False for _ in range(n)] for _ in range(n)], [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and visited_game[i][j] == False:
                game_board_empty.append(bfs(i,j,visited_game, game_board, 0))
            if table[i][j] == 1 and visited_table[i][j] == False:
                table_block.append(bfs(i,j,visited_table, table, 1))

    # 찾은 블록과 빈 공간들을 모두 0,0 기준으로 변환
    table_b = []
    for i in table_block:
        table_b.append(standard(i))

    game_b = []
    for i in game_board_empty:
        game_b.append(standard(i))


    for g in game_b:
        if g in table_b:
            answer += (len(g))
            table_b.remove(g)
        else:
            flag = False
            for t in table_b:
                import copy
                tmp = copy.copy(t)
                for _ in range(4): # 회전
                    if g == tmp:
                        answer += len(g)
                        table_b.remove(t)
                        flag=True
                        break
                    tmp = rotate(tmp)
                if flag:
                    break
    return answer

print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))



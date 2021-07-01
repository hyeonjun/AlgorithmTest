def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    def move(c1, c2):
        can_move = []
        # 평행이동 상 하 좌 우
        idx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in idx:
            n1 = (c1[0] + dx, c1[1] + dy)
            n2 = (c2[0] + dx, c2[1] + dy)
            if new_board[n1[0]][n1[1]] == 0 and new_board[n2[0]][n2[1]] == 0:
                can_move.append((n1, n2))

        # 회전
        if c1[0] == c2[0]:  # 가로 상태
            up, down = -1, 1
            for d in [up, down]:
                # 위와 아래가 모두 0인지 확인
                if new_board[c1[0] + d][c1[1]] == 0 and new_board[c2[0] + d][c2[1]] == 0:
                    can_move.append((c1, (c1[0]+d, c1[1]))) # 왼쪽 축 잡고 움직이기 -> 왼쪽 고정, 왼쪽 좌표에서 아래 or 위
                    can_move.append((c2, (c2[0]+d, c2[1]))) # 오른쪽 -
        else:  # 세로 상태
            left, right = -1, 1
            for d in [left, right]:
                if new_board[c1[0]][c1[1]+d] == 0 and new_board[c2[0]][c2[1]+d] == 0:
                    can_move.append((c1, (c1[0], c1[1]+d))) # 위쪽 고정
                    can_move.append((c2, (c2[0], c2[1]+d))) # 아래쪽 고정
        return can_move

    queue = [((1, 1), (1, 2), 0)]
    # visited = set([((1, 1), (1, 2))])
    visited = {((1, 1), (1, 2))}

    while queue:
        c1, c2, count = queue.pop(0)
        if c1 == (n, n) or c2 == (n, n):
            return count
        for i in move(c1, c2):
            if i not in visited:
                queue.append((*i, count + 1))
                visited.add(i)

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])) # 7
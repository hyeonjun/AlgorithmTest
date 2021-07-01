def solution(board, r, c):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])
    # row, coulmn, new board, count, enter_idx
    q = [(r, c, b, 0, -1)]
    s = set()

    def ctrl_move(b, y, x, dy, dx):
        ny, nx = y + dy, x + dx
        if 0 <= ny < 4 and 0 <= nx < 4 and b[ny * 4 + nx] == "0":
            return ctrl_move(b, ny, nx, dy, dx)
        else:
            if 0 <= ny < 4 and 0 <= nx < 4:
                return (ny, nx)
            else:
                return (y, x)

    while q:
        y, x, b, c, e = q.pop(0)
        pos = 4 * y + x

        if (y, x, b, e) in s:
            continue
        s.add((y, x, b, e))

        if b.count("0") == 16:  # game end
            return c

        # 한칸 이동
        for dy, dx in d:
            ny, nx = y + dy, x + dx
            if 0 <= ny < 4 and 0 <= nx < 4:
                q.append((ny, nx, b, c + 1, e))

        # ctrl 이동
        for dy, dx in d:
            ny, nx = ctrl_move(b, y, x, dy, dx)
            if ny == y and nx == x:
                continue
            q.append((ny, nx, b, c + 1, e))

        # enter
        if b[pos] != "0":
            if e == -1:
                q.append((y, x, b, c + 1, pos))
            else:
                if e != pos and b[e] == b[pos]:
                    b = b.replace(b[e], "0")
                    q.append((y, x, b, c + 1, -1))

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)) # 14
print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1)) # 16
n = 19
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1, 0), (1, 1), (0, 1), (-1, 1)]

def check():
    for x in range(n):
        for y in range(n):
            if board[x][y]:
                color = board[x][y]
                for dx, dy in direction:
                    nx, ny = x+dx, y+dy
                    count = 1
                    while 0 <= nx < n and 0 <= ny < n and color == board[nx][ny]:
                        count += 1
                        if count == 5:
                            if 0 <= nx + dx < n and 0 <= ny + dy < n and color == board[nx+dx][ny+dy]:
                                break
                            if 0 <= x - dx < n and 0 <= y - dy < n and color == board[x-dx][y-dy]:
                                break
                            return color, x+1, y+1
                        nx, ny = nx+dx, ny+dy
    return 0, -1, -1

color, x, y = check()
if not color:
    print(0)
else:
    print(color)
    print(x, y)
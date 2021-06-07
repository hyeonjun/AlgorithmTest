def solution(maps):
    row = len(maps)
    col = len(maps[0])

    answer = 0
    location = [[0, 0]]

    table = [[-1 for _ in range(col)] for _ in range(row)]
    table[0][0] = 1
    #       하       상       우       좌
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while location:
        y, x = location.pop(0)
        for i in range(4):
            ny = y + move[i][0]
            nx = x + move[i][1]

            if -1 < ny < row and -1 < nx < col:
                if maps[ny][nx] == 1:
                    if table[ny][nx] == -1:
                        table[ny][nx] = table[y][x] + 1
                        location.append([ny, nx])
    print(table)
    return table[-1][-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
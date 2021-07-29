# 늑대와 양
def solution(r, c, data):
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(r):
        for j in range(c):
            if data[i][j] == 'W':
                for dx, dy in move:
                    nx, ny = i+dx, j+dy
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        continue
                    if data[nx][ny] == 'S':
                        return 0, ''

    for i in range(r):
        for j in range(c):
            if data[i][j] not in 'SW':
                data[i][j] = 'D'
    return 1, [''.join(i) for i in data]

def sol_print(isCheck, data):
    if isCheck:
        print(isCheck)
        for i in data:
            print(i)
    else:
        print(isCheck)

data1 = [
['.', '.', 'S', '.', '.', '.'],
['.', '.', 'S', '.', 'W', '.'],
['.', 'S', '.', '.', '.', '.'],
['.', '.', 'W', '.', '.', '.'],
['.', '.', '.', 'W', '.', '.'],
['.', '.', '.', '.', '.', '.']]
isCheck, data = solution(6, 6, data1)
sol_print(isCheck, data)

data2 = [['S','W']]
isCheck, data = solution(1,2, data2)
sol_print(isCheck, data)

data3 = [
['.','S','.','.','.'],
['.','.','.','S','.'],
['S','.','.','.','.'],
['.','.','.','S','.'],
['.','S','.','.','.']
]
isCheck, data = solution(5,5, data3)
sol_print(isCheck, data)
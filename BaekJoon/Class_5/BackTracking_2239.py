puzzle = []
zero = []
for i in range(9):
    tmp = list(map(int, list(input())))
    puzzle.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            zero.append([i,j])

isEnd = False

def candidate(pos):
    num = [False] + [True for _ in range(9)] # 1~9 각 숫자가 들어갈 수 있는지

    # 작은 3*3 board에 있는 숫자들은 False로 해줌
    x, y = (pos[0]//3) * 3, (pos[1]//3) * 3
    for i in range(x, x+3):
        for j in range(y, y+3):
            num[puzzle[i][j]] = False

    # 가로줄, 세로줄에 있는 숫자들 False
    for i in range(9):
        num[puzzle[pos[0]][i]] = False
        num[puzzle[i][pos[1]]] = False

    return [i for i, v in enumerate(num) if v] # True인것들만 보낸다

def backtracking(k):
    global isEnd
    if k == len(zero): # 모두 다 채웠으면
        for i in puzzle:
            print(''.join(list(map(str, i))))
        isEnd = True
    else:
        for n in candidate(zero[k]):
            puzzle[zero[k][0]][zero[k][1]] = n
            backtracking(k+1)
            if isEnd:
                break
            puzzle[zero[k][0]][zero[k][1]] = 0

backtracking(0)
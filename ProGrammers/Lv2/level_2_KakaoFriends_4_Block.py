def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board))) # 세로로 내려와야하기때문에 행열을 바꿔서 해주는게 낫다

    def bomb(b):
        count = 0
        tmpB = [i[:] for i in b]
        for i in range(1, n):
            for j in range(1, m):
                if b[i][j] == -1: continue
                if b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] == b[i][j]:
                    tmpB[i - 1][j - 1], tmpB[i - 1][j], tmpB[i][j - 1], tmpB[i][j] = 0, 0, 0, 0

        for i, v in enumerate(tmpB):
            c = v.count(0)
            count += c
            tmpB[i] = [-1] * c + [a for a in v if a != 0] # 세로로 보기때문에 -1이 위로 올라가고 위에 있던 값이 아래로 내려오게 된다.
        return tmpB, count

    while True:
        board, count = bomb(board)
        if count == 0:
            return answer
        answer += count
    return answer

print(solution(4,5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
print(solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) # 15

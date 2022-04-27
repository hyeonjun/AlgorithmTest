# Solution1
# 짧을때는 빠르나 개수가 많아질수록 오래걸림
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    coordi = []
    for _ in range(n):
        x, y = map(int, input().split())
        coordi.append((x, y))
    coordi.sort(key=lambda x: x[0]) # x 좌표 기준 정렬
    answer = 0

    for i in range(n):
        tmp = []
        for j in range(i, n):
            if coordi[i][0] <= coordi[j][0] <= coordi[i][0]+10:
                tmp.append(coordi[j])
            else: break
        tmp.sort(key=lambda x: x[1]) # y 좌표 기준 정렬
        for k in range(len(tmp)):
            cnt = 0
            for l in range(k, len(tmp)):
                if tmp[k][1] <= tmp[l][1] <= tmp[k][1] + 10:
                    cnt += 1
                else: break
            answer = max(answer, cnt)
    print(answer)

# Solution2
import sys
input = sys.stdin.readline
board = [[0 for _ in range(10001)] for _ in range(10001)]
for _ in range(int(input())):
    n = int(input())

    answer = 0

    for _ in range(n):
        sx, sy = map(int, input().split())

        for x in range(sx, min(sx+10, 10000)+1):
            for y in range(sy, min(sy+10, 10000)+1):
                board[x][y] += 1

    for i in range(10001):
        for j in  range(10001):
            if not board[i][j]: continue
            answer = max(answer, board[i][j])
            board[i][j] = 0
    print(answer)

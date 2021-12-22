n = int(input())
color = [list(map(str, input().rstrip())) for _ in range(n)]

def check(color):
    cnt = 0
    for i in range(n):
        rowCnt = 1
        colCnt = 1
        for j in range(n - 1):
            if color[i][j] == color[i][j + 1]:
                rowCnt += 1
            else:
                cnt = max(cnt, rowCnt)
                rowCnt = 1
            if color[j][i] == color[j + 1][i]:
                colCnt += 1
            else:
                cnt = max(cnt, colCnt)
                colCnt = 1
        cnt = max(cnt, rowCnt, colCnt)
    return cnt


answer = 0
for i in range(n):
    for j in range(n - 1):
        if color[i][j] != color[i][j + 1]:
            color[i][j], color[i][j + 1] = color[i][j + 1], color[i][j]
            answer = max(answer, check(color))
            color[i][j], color[i][j + 1] = color[i][j + 1], color[i][j]
        if color[j][i] != color[j + 1][i]:
            color[j][i], color[j + 1][i] = color[j + 1][i], color[j][i]
            answer = max(answer, check(color))
            color[j][i], color[j + 1][i] = color[j + 1][i], color[j][i]

print(answer)
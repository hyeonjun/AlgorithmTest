n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0} # 아랫면 : 윗면
answer = 0

for i in range(6):
    topSide = dices[0][rotate[i]]
    side = [max(set([i for i in range(1, 7)]) - {dices[0][i], topSide})]
    for j in range(1, n):
        bottomSide, topSide = topSide, dices[j][rotate[dices[j].index(topSide)]]
        side.append(max(set([i for i in range(1, 7)]) - {bottomSide, topSide}))
    answer = max(answer, sum(side))
print(answer)
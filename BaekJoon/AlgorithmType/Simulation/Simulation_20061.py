n = int(input())
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

# t = 1, 1x1 / t = 2, 1x2 / t = 3, 2x1
def moveBlue(t, x):
    y = 0
    if t in (1, 2):
        for i in range(6):
            if blue[x][i]:
                break
            y += 1
        blue[x][y-1] = 1
        if t == 2:
            blue[x][y-2] = 1
    else:
        for i in range(6):
            if blue[x][i] or blue[x+1][i]:
                break
            y += 1
        blue[x][y-1], blue[x+1][y-1] = 1, 1

    checkBlue()
    for j in range(2):
        for i in range(4):
            if blue[i][j]:
                removeBlue(5)

def moveGreen(t, y):
    x = 0
    if t in (1, 3):
        for i in range(6):
            if green[i][y]:
                break
            x += 1
        green[x-1][y] = 1
        if t == 3:
            green[x-2][y] = 1
    else:
        for i in range(6):
            if green[i][y] or green[i][y+1]:
                break
            x += 1
        green[x-1][y], green[x-1][y+1] = 1, 1

    checkGreen()
    for i in range(2):
        for j in range(4):
            if green[i][j]:
                removeGreen(5)

def checkBlue():
    global answer
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if blue[i][j]:
                cnt += 1
        if cnt == 4:
            removeBlue(j)
            answer += 1

def checkGreen():
    global answer
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if green[i][j]:
                cnt += 1
        if cnt == 4:
            removeGreen(i)
            answer += 1

def removeBlue(idx):
    for j in range(idx, 0, -1):
        for i in range(4):
            blue[i][j] = blue[i][j-1]
    for i in range(4):
        blue[i][0] = 0

def removeGreen(idx):
    for i in range(idx, 0, -1):
        for j in range(4):
            green[i][j] = green[i-1][j]
    for j in range(4):
        green[0][j] = 0

answer = 0
count = 0
for _ in range(n):
    t, x, y = map(int, input().split())
    moveBlue(t, x)
    moveGreen(t, y)

count += sum(sum(b[2:]) for b in blue) + sum(sum(g) for g in green[2:])
print(answer)
print(count)
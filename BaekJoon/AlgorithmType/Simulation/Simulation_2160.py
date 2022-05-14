n = int(input())
boards = [[input() for _ in range(5)] for _ in range(n)]

def check(i, j):
    cnt = 0
    for x in range(5):
        for y in range(7):
            if boards[i][x][y] != boards[j][x][y]:
                cnt+=1
    return cnt

minV = 1e9
answer = []

for i in range(n-1):
    for j in range(i+1, n):
        cnt = check(i, j)
        if cnt < minV:
            minV = cnt
            answer = [i+1, j+1]
print(*answer)
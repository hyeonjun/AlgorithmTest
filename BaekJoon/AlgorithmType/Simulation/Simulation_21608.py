from collections import defaultdict
n = int(input())
board = [[0] * n for _ in range(n)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]
likeStudent = defaultdict(list)

for _ in range(n**2):
    arr = list(map(int, input().split()))
    likeStudent[arr[0]] = arr[1:]

    x, y = 0, 0
    maxC, maxE = -1, -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt = 0 # 해당 칸에 인접한 칸 중 좋아하는 학생 수
                empty = 0 # 인접한 칸 중 비어있는 칸 개수
                for dx, dy in direction:
                    nx, ny = i+dx, j+dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in likeStudent[arr[0]]:
                            cnt += 1
                        elif not board[nx][ny]:
                            empty += 1
                if maxC < cnt or (maxC == cnt and maxE < empty):
                    x, y = i, j
                    maxC, maxE = cnt, empty
    board[x][y] = arr[0]

answer = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        student = likeStudent[board[i][j]]
        for dx, dy in direction:
            nx, ny = i+dx, j+dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in student:
                cnt += 1
        answer += 10 ** (cnt-1) if cnt > 0 else 0
print(answer)

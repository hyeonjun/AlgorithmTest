board = [0 for _ in range(33)] # 도착 위치 지정
for i in range(21):
    board[i] = i+1
board[21] = 21 # 도착 지점
board[22:25] = [23, 24, 30]
board[25:27] = [26, 30]
board[27:30] = [28, 29, 30]
board[30:33] = [31, 32, 20]

score = [0 for _ in range(33)]
for i in range(1, 21):
    score[i] = i * 2
score[21] = 0
score[22:25] = [13, 16, 19]
score[25:27] = [22, 24]
score[27:30] = [28, 27, 26]
score[30:33] = [25, 30, 35]

dice = list(map(int, input().split()))
horse = [0, 0, 0, 0]
visited = [0 for _ in range(33)]

def dfs(depth, cnt):
    global answer
    if depth == 10:
        answer = max(answer, cnt)
        return

    for i in range(4): # 말
        # 말 현재 위치에서 주사위만큼 이동
        x, now_x, move = horse[i], horse[i], dice[depth]
        if x in [5, 10, 15]: # 안으로 들어갈 수 있는 위치
            if x == 5: x = 22
            elif x == 10: x = 25
            else: x = 27
            move -= 1
        if x + move <= 21: # 주사위 수만큼 이동했을 때 21 이하이면 한 번에 이동
            x += move
        else:
            for _ in range(move): # 21보다 크면 한 칸씩 이동(안쪽으로)
                x = board[x]

        if visited[x] and x != 21: # 이동한 위치가 끝이 아닌데 말이 있으면
            continue
        visited[now_x], visited[x], horse[i] = 0, 1, x
        dfs(depth+1, cnt+score[x])
        visited[now_x], visited[x], horse[i] = 1, 0, now_x
answer = 0
dfs(0, 0)
print(answer)

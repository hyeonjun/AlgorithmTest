def bfs():
    queue = [(0, 0)]
    door = [[] for _ in range(26)]
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    visited[0][0] = True
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < h+2 and 0 <= ny < w+2 and not visited[nx][ny] and board[nx][ny] != '*':
                visited[nx][ny] = True
                if board[nx][ny] == '$': # 문서
                    answer += 1
                elif board[nx][ny].islower(): # 열쇠
                    k = ord(board[nx][ny]) - ord('a')
                    keys[k] = True # 열쇠 획득
                    while door[k]: # 해당 열쇠로 열 수 있는 문이 있으면 모두 연다
                        doX, doY = door[k].pop(0)
                        queue.append((doX, doY)) # 문을 열고 다음 위치로 이동할 수 있게
                elif board[nx][ny].isupper(): # 문
                    d = ord(board[nx][ny]) - ord('A')
                    if not keys[d]: # 아직 해당 문의 열쇠를 얻지 못했으면
                        door[d].append((nx, ny))
                        continue
                    # 이미 얻어서 열 수 있으면 queue에 해당 위치를 추가하여 다음 위치로 이동할 수 있게 함
                queue.append((nx, ny))
    print(answer)

for _ in range(int(input())):
    h, w = map(int, input().split())
    # 처음에 빌딩의 외부에 시작하고, 빈 공간이나 열쇠로 열수 있는 문을 통해 출입할 수 있다.
    # 그래서 가로 세로를 확장해야 한다.
    board = [['.' for _ in range(w+2)]] # 빌딩의 바깥 위
    for _ in range(h):
        board.append(list('.'+input()+'.'))
    board.append(['.' for _ in range(w+2)])

    key = input()
    keys = [False for _ in range(26)]
    if key != '0':
        for k in key:
            keys[ord(k)-ord('a')] = True

    bfs()
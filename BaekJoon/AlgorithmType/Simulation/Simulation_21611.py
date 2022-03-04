import sys
input = sys.stdin.readline
n, m = map(int, input().split())
direction = [[],[-1, 0], [1, 0], [0, -1], [0, 1]]
board = [list(map(int, input().strip().split())) for _ in range(n)]
skill = [list(map(int, input().split())) for _ in range(m)]
answer = [0, 0, 0, 0]
position = []

def init():
    x, y = n//2, n//2
    position.append((x, y))
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    idx, step = 0, 0
    while True:
        if not idx % 2:
            step += 1
        flag = False
        for _ in range(step):
            x += dx[idx]
            y += dy[idx]
            position.append((x, y))
            if x == y == 0: # 끝까지 감
                flag = True
                break
        if flag: break
        idx = (idx + 1) % 4

def move():
    pos = []
    for x, y in position:
        if x == y == n//2: continue
        if board[x][y] == 0:
            pos.append((x, y))
        elif board[x][y] > 0 and pos:
            nx, ny = pos.pop(0)
            board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
            pos.append((x, y))

def bomb():
    visited = []
    flag = False
    cnt = 0
    num = -1
    for x, y in position:
        if x == y == n//2: continue
        if num == board[x][y]:
            visited.append((x, y))
            cnt += 1
        else:
            if cnt >= 4:
                flag = True
                answer[num] += cnt
            while visited:
                vx, vy = visited.pop(0)
                if cnt >= 4: board[vx][vy] = 0
            cnt = 1
            num = board[x][y]
            visited.append((x, y))
    return flag

def group(): # 구슬 A의 번호는 그룹에 들어있는 구슬의 개수이고, B는 그룹을 이루고 있는 구슬의 번호
    num = -1
    cnt = 0
    nums = [0]
    for x, y in position:
        if x == y == n//2: continue
        if num == -1:
            num = board[x][y]
            cnt = 1
        else:
            if num == board[x][y]:
                cnt += 1
            else:
                nums.extend([cnt, num])
                cnt = 1
                num = board[x][y]
    idx = 0
    for x, y in position:
        board[x][y] = nums[idx]
        idx += 1
        if idx >= len(nums): break

def simulation():
    for d, s in skill:
        x, y = n//2, n //2
        # 마법 시전
        for i in range(1, s+1):
            nx = x + (i * direction[d][0])
            ny = y + (i * direction[d][1])
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 0

        # 구슬 이동
        move()

        # 연속 구슬 4개 있는지 확인 -> 폭발
        while bomb():
            move()

        # 구글 그룹 -> board 채움
        group()

init()
simulation()
print(sum(i*answer[i] for i in range(4)))

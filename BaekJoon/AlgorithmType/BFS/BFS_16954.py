### Solution 1 - 1108ms
from collections import deque
board = deque([list(input()) for _ in range(8)])
direction = [(0, 0), (1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def down():
    board.pop()
    board.appendleft(['.' for _ in range(8)])

def bfs():
    queue = deque([(7, 0)])
    downCnt = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] == '#':
                continue
            if (x, y) == (0, 7):
                return 1
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == '.':
                    queue.append((nx, ny))
        down()
        downCnt += 1
        if downCnt > 8:
            return 1
    return 0

print(bfs())

### Solution 2 - 140ms
from collections import deque
board = []
wall = set()
for i in range(8):
    tmp = list(input())
    for j in range(8):
        if tmp[j] == '#':
            wall.add((i, j))
    board.append(tmp)

direction = [(0, 0), (1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def bfs():
    global wall
    queue = deque([(7, 0)])
    visited = set()
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) in wall:
                continue
            if (x, y) == (0, 7):
                return 1
            for dx, dy in direction:
                nx, ny = x+dx, y+dy
                if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited and (nx, ny) not in wall:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        if wall: # 벽이 있으면 방문 표시 초기화
            visited.clear()
        tmp = set()
        for i, j in wall: # 다음 위치에 있는 벽 집합 만듬
            if i < 7:
                tmp.add((i+1, j))
        wall = tmp # 업데이트
    return 0
print(bfs())
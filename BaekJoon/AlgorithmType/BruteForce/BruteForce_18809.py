from itertools import combinations
import sys
input = sys.stdin.readline
n, m, g, r = map(int, input().split())
possible = []
board = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 2:
            possible.append((i, j))
    board.append(tmp)

direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    result = 0
    queue = []
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)] # 시간, 상태
    for x, y in R:
        queue.append((x, y))
        visited[x][y][1] = 1
    for x, y in G:
        queue.append((x, y))
        visited[x][y][1] = 2

    while queue:
        x, y = queue.pop(0)
        if visited[x][y][1] == 3: # 이미 꽃
            continue
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0: # 호수
                    continue
                if visited[nx][ny][1] == 0:
                    visited[nx][ny][0] = visited[x][y][0]+1
                    visited[nx][ny][1] = visited[x][y][1]
                    queue.append((nx, ny))
                elif (visited[nx][ny][1] == 1 and visited[x][y][1] == 2)\
                        or (visited[nx][ny][1] == 2 and visited[x][y][1] == 1):
                    if visited[nx][ny][0] == visited[x][y][0]+1: # 같은 시간에 퍼지면 꽃
                        visited[nx][ny][1] = 3
                        result += 1
    return result

answer = 0
for c1 in combinations(range(len(possible)), r+g):
    for c2 in combinations(range(r+g), r):
        R, G = [], []
        for i in range(r+g):
            if i in c2:
                R.append(possible[c1[i]])
            else:
                G.append(possible[c1[i]])
        answer = max(answer, bfs())
print(answer)
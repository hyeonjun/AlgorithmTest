from copy import deepcopy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
virus_possible = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            tmp[j] = -2
        elif tmp[j] == 2:
            virus_possible.append((i, j))
            tmp[j] = -1
        else:
            tmp[j] = -1
    board.append(tmp)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check():
    result = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                return -1
            if (i, j) not in virus_possible:
                result = max(result, matrix[i][j])
    return result

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == -1:
                matrix[nx][ny] = matrix[x][y] +1
                queue.append((nx, ny))
    return check()

answer = 1e9
for c in combinations(virus_possible, m):
    matrix = deepcopy(board)
    for x, y in c:
        matrix[x][y] = 0
    result = bfs(deque(list(c)))
    if result != -1:
        answer = min(answer, result)
print(answer if answer != 1e9 else -1)
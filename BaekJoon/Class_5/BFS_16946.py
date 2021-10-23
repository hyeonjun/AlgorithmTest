"""
board를 bfs로 완전 탐색 -> 0을 시작으로 함, 인접 빈칸 개수를 세어
리스트에 기록.
"""
import sys
from collections import deque
input = sys.stdin.readline
direction = [(1,0), (0,1), (-1,0), (0,-1)]
n, m = map(int, input().strip().split())

def bfs(i, j):
    queue = deque([[i, j]])
    visited[i][j] = True
    cnt = 1
    while queue:
        x, y = queue.popleft()
        zero[x][y] = group
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 0:
                queue.append([nx, ny])
                cnt += 1
                visited[nx][ny] =True
    return cnt

def count(x, y): # 움직일 수 있는 위치 개수 세기
    move = set() # 중복제거를 위해
    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and zero[nx][ny] != 0:
            move.add(zero[nx][ny]) # 더해야할 그룹 인덱스 추가
    cnt = 1
    for i in move: # 그룹 돌면서 cnt 더하기
        cnt += info[i]
        cnt %= 10
    return cnt

board = [list(map(int, input().strip())) for _ in range(n)]

"""
0 0 1 1 0
2 2 0 0 0
2 0 3 0 4
0 5 0 6 0
"""
visited = [[0 for _ in range(m)] for _ in range(n)]
zero = [[0 for _ in range(m)] for _ in range(n)] # 인접한 0끼리 같은 그룹으로 묶어서 표시
group = 1
info = {}
for i in range(n):
    for j in range(m):
            if board[i][j] == 0 and not visited[i][j]:
                info[group] = bfs(i, j)
                group += 1
answer = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            answer[i][j] = count(i, j)

for i in answer:
    print(''.join(map(str, i)))

"""
벽인 1인 지점을 찾아서 bfs시도
주변 0인 지점을 찾음 +1
 => 시간 초과
"""
# from collections import deque
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().strip().split())
# board = [list(map(int, list(input().strip()))) for _ in range(n)]
# answer = [[0 for _ in range(m)] for _ in range(n)]
# direction = [(1,0), (0,1), (-1,0), (0,-1)]
# start = []
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 1:
#             answer[i][j] = 1
#             start.append([i, j])
#
# def bfs(i, j, cnt):
#     queue = deque([[i, j]])
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     visited[i][j] = True
#     while queue:
#         x, y = queue.popleft()
#         for dx, dy in direction:
#             nx, ny = x+dx, y+dy
#             if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny] == 0:
#                 visited[nx][ny] = True
#                 cnt += 1
#                 queue.append([nx, ny])
#     return cnt % 10
#
# for i, j in start:
#     answer[i][j] = bfs(i, j, 1)
#
# for i in answer:
#     print(''.join(map(str, i)))
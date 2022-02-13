from collections import deque
n, m, k = map(int, input().split())
A = [[5 for _ in range(n)] for _ in range(n)]
appendA = [list(map(int, input().split())) for _ in range(n)]
board = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    board[x-1][y-1].append(z)

direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulation():
    # 봄, 여름
    for r in range(n):
        for c in range(n):
            length = len(board[r][c])
            for i in range(length):
                if A[r][c] >= board[r][c][i]:
                    A[r][c] -= board[r][c][i]
                    board[r][c][i] += 1
                else:
                    for _ in range(i, length):
                        A[r][c] += board[r][c].pop() // 2
                    break

    # 가을, 겨울
    for r in range(n):
        for c in range(n):
            for i in board[r][c]:
                if i % 5 == 0:
                    for dx, dy in direction:
                        nx, ny = r+dx, c+dy
                        if 0 <= nx < n and 0 <= ny < n:
                            board[nx][ny].appendleft(1)
            A[r][c] += appendA[r][c]

for _ in range(k):
    simulation()

answer = 0
for b in board:
    for i in b:
        answer += len(i)
print(answer)

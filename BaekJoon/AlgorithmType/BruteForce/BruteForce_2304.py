n = int(input())
board = [0 for _ in range(1001)]
max_height, center = 0, 0
last_idx = 0
for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y
    if max_height < y:
        max_height = y
        center = x
    last_idx = max(x, last_idx)
height = 0
answer = 0
for i in range(1, center): # 왼쪽
    height = max(height, board[i])
    answer += height

height = 0
for i in range(last_idx, center, -1): # 오른쪽
    height = max(height, board[i])
    answer += height

print(answer+max_height)
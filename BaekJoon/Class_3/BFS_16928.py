import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [0 for _ in range(101)]
visited = [False for _ in range(101)]
jump = dict()
for _ in range(n+m):
    x, y = map(int, input().split())
    jump[x] = y

def bfs():
    queue = [1]
    visited[1] = True
    while queue:
        x = queue.pop(0)
        for dx in range(1, 7): # 주사위
            nx = x + dx
            if nx > 100 or visited[nx]:
                continue
            if nx in jump:
                nx = jump[nx]
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                board[nx] = board[x] + 1

bfs()
print(board[100])


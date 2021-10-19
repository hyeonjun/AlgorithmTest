import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dirention = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs(i, j, visited):
    answer = 1
    queue = set([(i, j, visited)])
    while queue:
        x, y, visited = queue.pop()
        answer = max(answer, len(visited))
        for dx, dy in dirention:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in visited:
                queue.add((nx, ny, visited+board[nx][ny]))
    return answer

print(bfs(0,0,board[0][0]))
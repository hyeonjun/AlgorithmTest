n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1,0), (-1,0), (0,1), (0,-1)]
def bfs():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    gram = 1e9
    queue = [(0, 0)]
    visited[0][0] = 1
    while queue:
        x, y = queue.pop(0)
        if board[x][y] == 2:
            gram = (n-1)-x + (m-1)-y + visited[x][y]-1
        if x == n-1 and y == m-1:
            return min(gram, visited[x][y]-1)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return gram

answer = bfs()
if answer > t:
    print("Fail")
else:
    print(answer)
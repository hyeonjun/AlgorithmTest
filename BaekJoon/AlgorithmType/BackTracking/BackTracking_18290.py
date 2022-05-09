import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = -1e9
visited = [[False for _ in range(m)] for _ in range(n)]
def dfs(x, y, cnt, value):
    global answer
    if cnt == k:
        answer = max(answer, value)
        return

    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if visited[i][j]:
                continue
            for dx, dy in direction: # 인접 위치 칸을 선택했는지 확인
                nx, ny = i+dx, j+dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    break
            else:
                visited[i][j] = True
                dfs(i, j, cnt+1, value+board[i][j])
                visited[i][j] = False
dfs(0, 0, 0, 0)
print(answer)
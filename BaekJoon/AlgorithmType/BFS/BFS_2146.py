n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_grouping(x, y, num):
    queue = [(x, y)]
    visited[x][y] = True
    group = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                group.append((nx, ny))
                queue.append((nx, ny))
    return group

groups = []
nums = 1
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            g = bfs_grouping(i, j, nums)
            groups.append(g)
            nums += 1

def bfs_distance(queue: list):
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    for x, y in queue:
        distance[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and distance[nx][ny] == -1:
                if not board[nx][ny]: # 바다
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                else:
                    return distance[x][y]

answer = 1e9
for group in groups:
    answer = min(answer, bfs_distance(group))
print(answer)
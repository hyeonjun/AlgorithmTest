n, m = map(int, input().split())
map = [list(map(int, list(input()))) for _ in range(n)]

direction = [(1,0), (0,1), (-1,0), (0,-1)]
def bfs():
    queue = [(0,0,0)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    while queue:
        x, y, z = queue.pop(0)
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 > nx or n <= nx or 0 > ny or m <= ny:
                continue
            if map[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            elif z == 0 and map[nx][ny] == 1 and visited[nx][ny][1] == 0: # 벽 뿌수고 지나가기
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))
    return -1

print(bfs())

"""
13 13
0100011011000
0001001010000
0000100001000
1100010101011
1111101111000
1011010001001
0100001001001
0100111010001
0101010000100
0001110100000
0000001000100
1010001000111
1001000100000

=> 27
"""
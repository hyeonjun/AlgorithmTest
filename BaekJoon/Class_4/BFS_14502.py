"""
벽을 세울 수 있는 곳에 세 개의 벽을 세우면서 -> 조합
바이러스를 퍼지게 한 뒤 안전영역을 구한다 -> bfs
이를 반복해서 벽을 세울 수 있는 모든 경우의 수에 대해서
안전 영역을 구해 max값을 출력한다.
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
direction = [(1,0), (-1, 0), (0,1), (0,-1)]
maxV = 0

# ===================================================================
# 벽 세우기
def select_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                select_wall(count+1)
                graph[i][j] = 0

def bfs():
    global maxV
    # tmp_graph = copy.deepcopy(graph) # 시간 3364
    tmp_graph = [i[:] for i in graph] # 시간 2088
    queue = []
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.pop(0)
        for dx, dy in direction:
            nx, ny = dx + x, dy + y
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2 # 바이러스 퍼짐
                queue.append((nx, ny))

    maxV = max(maxV, sum(i.count(0) for i in tmp_graph))

select_wall(0)
print(maxV)

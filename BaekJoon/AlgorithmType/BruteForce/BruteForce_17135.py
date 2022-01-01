from itertools import combinations
import heapq
from copy import deepcopy
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
archer = list(combinations([i for i in range(m)], 3))
answer = 0
def move():
    global tmp
    new = [0 for _ in range(m)]
    tmp[-1] = new
    for i in range(n-2, -1, -1):
        tmp[i+1] = tmp[i]
    tmp[0] = new

def attack(archer):
    global tmp
    cnt = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    remove = []
    for a in archer:
        heap = []
        for x in range(n-1, -1, -1):
            for y in range(m):
                if tmp[x][y]:
                    dist = abs(n-x) + abs(a-y)
                    if dist <= d:
                        heapq.heappush(heap, [dist, y, x]) # 가장 가까이 있으면서 가장 왼쪽이여야 한다.
        if heap:
            _, y, x = heapq.heappop(heap)
            remove.append([x, y])
    for x, y in remove:
        if not visited[x][y]:
            visited[x][y] = True
            cnt += 1
            tmp[x][y] = 0
    return cnt

def count_enemy(): # 시뮬레이션 끝
    global tmp
    for i in tmp:
        if sum(i) > 0:
            return False
    return True

def simulation(archer):
    result = 0
    while not count_enemy():
        result += attack(archer)
        move()
    return result

for a in archer:
    tmp = deepcopy(board)
    answer = max(answer, simulation(a))
print(answer)
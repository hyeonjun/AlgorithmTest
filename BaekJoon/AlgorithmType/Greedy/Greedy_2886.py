import sys
import heapq
input = sys.stdin.readline
r, c = map(int, input().split())
board = []
people, chair = [], []
for i in range(r):
    tmp = list(input())
    for j in range(c):
        if tmp[j] == 'X':
            people.append((i, j))
        elif tmp[j] == 'L':
            chair.append((i, j))
    board.append(tmp)

heap = []
# 각 사람과 의자 거리 기준으로 우선순위 큐
for px, py in people:
    for cx, cy in chair:
        dist = (px - cx) ** 2 + (py - cy) ** 2
        heapq.heappush(heap, (dist, (px, py), (cx, cy)))

c_visited = [[1e9 for _ in range(c)] for _ in range(r)]
p_visited = [[False for _ in range(c)] for _ in range(r)]
fight = [[0 for _ in range(c)] for _ in range(r)]

answer = 0

while heap:
    d, p, c = heapq.heappop(heap)
    if not p_visited[p[0]][p[1]] and d <= c_visited[c[0]][c[1]]:
        c_visited[c[0]][c[1]] = d
        p_visited[p[0]][p[1]] = True
        fight[c[0]][c[1]] += 1
        if fight[c[0]][c[1]] == 2:
            answer += 1
print(answer)
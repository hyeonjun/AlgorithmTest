"""
정사각형일 경우 '123456780'로 하는 것이 더 빠르다.
row = idx // 3
col = idx % 3
visited = dict()를 해서 경로를 확인하면 list보다 더 빠르게 확인할 수 있음

"""
puzzle = ''
for _ in range(3):
    tmp = input().replace(' ', '')
    puzzle += tmp
direction = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs():
    queue = [puzzle]
    visited = {puzzle:0}
    while queue:
        p = queue.pop(0)
        if p == '123456780':
            return visited[p]
        idx = p.find('0')
        x, y = idx//3, idx%3 # idx를 좌표로
        for dx, dy in direction:
            nx, ny = dx+x, dy+y
            if 0 <= nx < 3 and 0 <= ny < 3:
                nd = nx * 3 + ny # 좌표를 문자열 idx로
                np = list(p)
                np[idx], np[nd] = np[nd], np[idx] # swap
                np = ''.join(np)
                if not visited.get(np):
                    visited[np] = visited[p] + 1
                    queue.append(np)
    return -1
print(bfs())
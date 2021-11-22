a, b, c = map(int, input().split())
visited = [[False for _ in range(b+1)] for _ in range(a+1)]
answer = []
queue = [[0,0,c]]

def bfs():
    while queue:
        x, y, z = queue.pop(0)
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == 0:
            answer.append(z)
        if x + y > b:
            queue.append([x + y - b, b, z])
        else:
            queue.append([0, x + y, z])
        if x + z > c:
            queue.append([x + z - c, y, c])
        else:
            queue.append([0, y, x + z])
        if y + x > a:
            queue.append([a, y + x - a, z])
        else:
            queue.append([y + x, 0, z])
        if y + z > c:
            queue.append([x, y + z - c, c])
        else:
            queue.append([x, 0, y + z])
        if z + x > a:
            queue.append([a, y, z + x - a])
        else:
            queue.append([z + x, y, 0])
        if z + y > b:
            queue.append([x, b, z + y - b])
        else:
            queue.append([x, z + y, 0])
bfs()

for i in sorted(answer):
    print(i, end=" ")
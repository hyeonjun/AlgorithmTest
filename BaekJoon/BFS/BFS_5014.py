f, s, g, u, d = map(int, input().split()) # 총 노드, 현재위치, 목표, 이동 방법1, 2

visited = [0 for _ in range(f+1)]
queue = [s]
visited[s] = 1


while queue:
    x = queue.pop(0)
    if x == g:
        break
    for dx in [u, -d]:
        nx = x+dx
        if 1 <= nx <= f and not visited[nx]:
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(visited[g]-1 if visited[g] != 0 else "use the stairs")
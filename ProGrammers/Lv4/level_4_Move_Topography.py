def solution(land, height):
    import heapq
    n = len(land)

    visited = [[False for _ in range(n)] for _ in range(n)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(0, 0, 0)]

    visit_count = 0  # 방문 횟수
    max_count = n * n  # 최대 방문 횟수
    value = 0  # 사다리 비용

    while visit_count < max_count:
        v, y, x = heapq.heappop(queue)
        if visited[y][x]:
            continue
        visited[y][x] = True  # 방문
        visit_count += 1
        value += v

        c_h = land[y][x]  # 현 좌표 height
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if not visited[ny][nx]:
                n_h = land[ny][nx]
                if abs(n_h - c_h) > height:  # 사다리 필요?
                    heapq.heappush(queue, (abs(n_h - c_h), ny, nx))
                else:
                    heapq.heappush(queue, (0, ny, nx))

    return value

land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
print(solution(land, 3)) # 15

land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
print(solution(land, 1)) # 18
n, k = map(int, input().split())

def bfs():
    queue = [n]
    distances = [-1 for _ in range(100001)]
    distances[n] = 0

    while queue:
        x = queue.pop(0)
        if x == k:
            return distances[x]
        if 0 <= x * 2 < 100001 and distances[x * 2] == -1:
            distances[x*2] = distances[x] # 시간 0
            queue.append(x*2)
        for i in (x-1, x+1):
            if 0 <= i < 100001 and distances[i] == -1:
                distances[i] = distances[x] + 1 # 시간 1
                queue.append(i)

print(bfs())

def dijkstra():
    import heapq
    queue = []
    heapq.heappush(queue, (0, n))
    dist = [1e9 for _ in range(100001)]
    dist[n] = 0
    while queue:
        now_d, now_n = heapq.heappop(queue)
        if 0 <= now_n * 2 < 100001 and dist[now_n * 2] == 1e9:
            dist[now_n * 2] = dist[now_n]
            heapq.heappush(queue, (dist[now_n * 2], now_n * 2))
        for next_n in (now_n+1, now_n-1):
            if 0 <= next_n < 100001 and dist[next_n] == 1e9:
                dist[next_n] = now_d+1
                heapq.heappush(queue, (dist[next_n], next_n))
    return dist[k]

print(dijkstra())
import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((d, b))

s, e = map(int, input().split())

def dijstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = [1e9 for _ in range(n+1)]
    distances[start] = 0
    path = [[] for _ in range(n+1)]
    path[start].append(start)

    while queue:
        now_d, now_n = queue.pop(0)
        if now_d > distances[now_n]:
            continue
        for next_d, next_n in graph[now_n]:
            next_d += now_d
            if distances[next_n] > next_d:
                distances[next_n] = next_d
                heapq.heappush(queue, (next_d, next_n))
                path[next_n] = []
                for p in path[now_n]:
                    path[next_n].append(p)
                path[next_n].append(next_n)

    return distances, path

dis, route = dijstra(s)
print(dis[e])
print(len(route[e]))
print(' '.join(map(str, route[e])))
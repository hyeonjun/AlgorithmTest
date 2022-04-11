from collections import deque
n, k = map(int, input().split())
history = [0 for _ in range(100001)]

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = [0 for _ in range(100001)]
    visited[start] = 1
    while queue:
        for _ in range(len(queue)):
            x, cnt = queue.popleft()
            if x == end:
                result = []
                while x != start:
                    result.append(x)
                    x = history[x]
                return cnt, [start] + result[::-1]
            for y in (x-1, x+1, x*2):
                if 0 <= y < 100001 and not visited[y]:
                    queue.append((y, cnt+1))
                    history[y] = x
                    visited[y] = 1

time, his = bfs(n, k)
print(time)
print(*his)
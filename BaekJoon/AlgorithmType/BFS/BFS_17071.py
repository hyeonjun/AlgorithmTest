from collections import deque
n, k = map(int, input().split())

def bfs(n, k):
    queue = deque([n])
    visited = [[0 for _ in range(500001)] for _ in range(2)] # 재방문 허용
    visited[0][n] = 1
    flag = 0
    time = 0
    while queue:
        if k > 500000: return -1
        if visited[flag][k]: return time
        tmp = deque()
        flag = 1-flag
        for _ in range(len(queue)):
            x = queue.popleft()
            for nx in (x-1, x+1, x*2):
                if 0 <= nx < 500001 and not visited[flag][nx]:
                    tmp.append(nx)
                    visited[flag][nx] = 1
        time += 1
        k += time
        queue = tmp
    return -1
print(bfs(n, k))

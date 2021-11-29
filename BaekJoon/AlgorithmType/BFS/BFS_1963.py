prime = [True for _ in range(10000)]
for i in range(2, 100):
    if prime[i]:
        for j in range(i*2, 10000, i):
            prime[j] = False

def bfs():
    queue = [(start, 0)]
    visited[start] = True
    while queue:
        x, cnt = queue.pop(0)
        if x == target:
            return cnt
        for i in range(4):
            for j in range(10):
                dx = int(str(x)[:i] + str(j) + str(x)[i+1:])
                if not visited[dx] and prime[dx] and dx >= 1000:
                    visited[dx] = True
                    queue.append((dx, cnt+1))
    return -1


for _ in range(int(input())):
    start, target = map(int, input().split())
    visited = [False for _ in range(10000)]
    answer = bfs()
    print(answer if answer != -1 else "Impossible")
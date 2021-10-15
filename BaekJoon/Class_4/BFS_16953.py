a, b = map(int, input().split())

def bfs():
    queue = [(a, 1)]
    while queue:
        x, cnt = queue.pop(0)
        if x == b:
            return cnt
        for i in (x*2, int(str(x)+'1')):
            if 0 <= i < b+1:
                queue.append((i, cnt+1))
    return -1
print(bfs())
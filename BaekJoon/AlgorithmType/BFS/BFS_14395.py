s, t = map(int, input().split())

def bfs():
    queue = [(s, '')]
    visited = {s}
    while queue:
        x, path = queue.pop(0)
        if x == t:
            return path

        for op in ('*', '+', '/'): # -의 경우 값이 빠지기 때문에 최소 연산 횟수를 벗어나게 된다
            if op == '*':
                nx = x * x
            elif op == '+':
                nx = x + x
            else:
                nx = 1
            if 0 <= nx <= t and nx not in visited:
                visited.add(nx)
                queue.append((nx, path+op))
    return -1

if s == t:
    print(0)
else:
    print(bfs())
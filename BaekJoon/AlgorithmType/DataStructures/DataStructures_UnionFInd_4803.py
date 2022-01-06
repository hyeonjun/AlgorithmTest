def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

idx = 1
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    parent = list(range(n+1))
    cycle = []
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b): # 사이클 발생
            cycle.append(a)
            continue
        union(a, b)

    # 갱신
    for i in range(1, n+1):
        find(i)

    cycleGroup = set()
    for c in cycle:
        cycleGroup.add(parent[c])

    answer = 0
    for i in range(1, n+1):
        if parent[i] in cycleGroup:
            continue
        answer += 1
        cycleGroup.add(parent[i])

    if answer == 0:
        print(f'Case {idx}: No trees.')
    elif answer == 1:
        print(f'Case {idx}: There is one tree.')
    else:
        print(f'Case {idx}: A forest of {answer} trees.')
    idx += 1
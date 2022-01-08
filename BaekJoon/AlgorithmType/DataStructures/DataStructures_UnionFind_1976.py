n = int(input())
m = int(input())

parent = list(range(n+1))

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

for i in range(1, n+1):
    graph = list(map(int, input().split()))
    for j in range(1, n+1):
        if graph[j-1] == 1:
            union(i, j)

arr = list(map(int, input().split()))
answer = set()
for i in arr:
    answer.add(find(i))
if len(answer) == 1:
    print("YES")
else:
    print("NO")

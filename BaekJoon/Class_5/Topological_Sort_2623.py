n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
for _ in range(m):
    arr = list(map(int, input().split()))[1:]
    for i in range(len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        degree[arr[i+1]] += 1

queue = []
for i in range(1,n+1):
    if degree[i] == 0:
        queue.append(i)
answer = []
while queue:
    x = queue.pop(0)
    answer.append(x)
    for i in graph[x]:
        degree[i] -= 1
        if degree[i] == 0:
            queue.append(i)

if len(answer) != n:
    print(0)
else:
    for i in answer:
        print(i)
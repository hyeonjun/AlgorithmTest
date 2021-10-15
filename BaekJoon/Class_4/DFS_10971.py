import sys
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = 1e9

def dfs(i, k, distance):
    global result

    # if all(visited):
    if len(visited) == n:
        if matrix[k][i] != 0: # 돌아갈 수 없는 경우는 없애야함
            result = min(result, distance + matrix[k][i]) # 돌아가는 비용 더해서 구함
        return

    for j in range(n):
        # if matrix[k][j] != 0 and i != j and not visited[j]:
        if matrix[k][j] != 0 and i != j and j not in visited:
            visited.append(j)
            dfs(i, j, distance + matrix[k][j])
            visited.pop()

for i in range(n):
    visited = [i]
    # visited = [False for _ in range(n)]
    # visited[i] = True
    dfs(i, i, 0)
print(result)
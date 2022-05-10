import sys
input=sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[[] for _ in range(n+1)] for _ in range(2)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[0][b].append(a) # 자신보다 앞 등수인 애들
    graph[1][a].append(b) # 자신보다 뒷 등수인 애들

def dfs(type, idx):
    result = 1
    visited[idx] = True
    for i in graph[type][idx]: # type에 따라 자신보다 확실하게 앞이나 뒤인 노드 개수를 구하면 된다
        if not visited[i]:
            result += dfs(type, i)
    return result

# visited는 앞등수와 뒷등수 노드가 완전히 다른 노드들이기 때문에 새롭게 초기화할 필요 없음
visited = [False for _ in range(n+1)]
ans1 = dfs(0, x)
ans2 = n - dfs(1, x) + 1
print(ans1, ans2)
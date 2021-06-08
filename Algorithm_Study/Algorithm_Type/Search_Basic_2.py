# -*- coding:cp949 -*-
# 공유기 설치
def solution(h, r, home):
    home = sorted(home)
    start = 1
    end = home[-1] - home[0]
    result = 0

    while start <= end:
        mid = (start+end) // 2
        value = home[0]
        count = 1
        for i in range(1, len(home)):
            if home[i] >= value+mid:
                value = home[i]
                count += 1
        if count >= r:
            start = mid +1
            result = mid
        else:
            end = mid-1
    return result

# h, r = list(map(int, input().split(' ')))
# home = []
# for _ in range(h):
#     home.append(int(input()))
# print(solution(h, r, home))

print(solution(5,3,[1,2,8,4,9])) # 3

# ===========================================================================

# 중량제한
def solution(n,m,data, start_node,end_node):
    adj = [[] for _ in range(n+1)]
    start = data[0][2]
    end = data[0][2]
    for x,y,weight in data:
        adj[x].append((y,weight))
        adj[y].append((x,weight))
        start = min(start, weight)
        end = max(end, weight)
    result = start

    def bfs(c):
        queue = [start_node]
        visited = [False] * (n + 1)
        visited[start_node] = True
        while queue:
            x = queue.pop(0)
            for y, weight in adj[x]:
                if not visited[y] and weight >= c:
                    visited[y] = True
                    queue.append(y)
        return visited[end_node]

    while start <= end:
        mid = (start+end)//2
        if bfs(mid): # 이동 가능?
            result = mid
            start = mid +1
        else:
            end = mid -1
    return result

print(solution(3,3,[[1,2,2],[3,1,3],[2,3,2]],1,3))



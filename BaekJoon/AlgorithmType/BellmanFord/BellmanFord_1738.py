n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

def bf(start):
    global n
    # 이 문제는 최단 거리가 아닌 최대 금품이기 때문에 1e9가 아닌 -1e9로 초기화
    distance = [-float('inf') for _ in range(n + 1)]
    distance[start] = 0
    route = [0 for _ in range(n+1)]
    for check in range(n):
        for now_n in range(1, n+1):
            for next_d, next_n in graph[now_n]:
                next_d += distance[now_n]
                if distance[now_n] != 1e9 and distance[next_n] < next_d:
                    distance[next_n] = next_d
                    route[next_n] = now_n
                    if check == n-1: # 사이클이 존재한다고 무조건 return 해서는 안된다. 루트에서 n번 노드에 도달할 수 있는 노드인가를 봐야한다.
                        distance[next_n] = float('inf') # 그래서 사이클이 있는 경우 도착 도느의 distance 값을 1e9로 설정해준다.
    if distance[n] == float('inf'): # 1e9이면 n번 노드로 가는데 사이클을 통한 루트가 있는 것이므로 -1을 출력함
        return [-1]
    else:
        answer = [n] # n부터 역으로 answer에 담음
        while n != 1:
            n = route[n]
            answer.append(n)
        return answer[::-1]

print(*bf(1))
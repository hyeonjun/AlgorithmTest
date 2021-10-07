"""
* 벨만-포드 알고리즘 : 그래프에서 시작 정점으로부터 다른 정점까지의 최단 경로를 찾기 위한 알고리즘.
1. 음수 가중치가 있는 그래프의 시작 정점에서 다른 정점까지의 최단 거리를 구할 수 있다.
2. 음수 사이클 존재의 여부를 알 수 있다.


"""
def bellman_ford(start):
    distances = [1e9 for _ in range(n+1)]
    distances[start] = 0

    for check in range(n): # 모든 정점에 대해서 자신의 정점까지의 거리가 적은 것으로 갱신되는 것을 정점 개수만큼 반복
        for now_n in range(1, n+1): # 지점
            for next_d, next_n in adj[now_n]:
                next_d += distances[now_n]
                if next_d < distances[next_n]:
                    distances[next_n] = next_d
                    # 계속 줄어들어 n번째까지 값이 갱신되다면 "음의 싸이클"이 존재하므로 출발하였을 때보다 시간이 되돌아가 있게 된다.
                    if check == n-1:
                        return False
    return True


for _ in range(int(input())):
    n, m, w = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        s, e, d = map(int, input().split())
        adj[s].append((d, e))
        adj[e].append((d, s))

    for _ in range(w):
        s, e, d = map(int, input().split())
        adj[s].append((-d, e))

    print("NO") if bellman_ford(1) else print("YES")
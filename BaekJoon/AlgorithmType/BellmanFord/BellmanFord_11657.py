"""
벨만-포드 알고리즘
- 시작 노드에 대해서 거리를 0으로 초기화. 나머지 노드 거리를 무한으로 설정
- 정점 수(N) - 1만큼 다음과정을 반복
- 매 반복마다 모든 간선 확인
- 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, 거리 정보 갱신
- N-1번 반복 후, N 번째 반복에서도 거리 값이 갱신된다면 음수 순환 존재
- 다익스트라와의 차이점은 매 반복마다 모든 간선을 확인한다는 것
- 다익스트라의 경우 방문하지 않는 노드 중에서 최단 거리가 가장 가까운 노드만을 방문함
"""

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))


def bf(start):
    distance[start] = 0

    for check in range(n):
        for now_n in range(1, n + 1):
            for next_d, next_n in graph[now_n]:
                if distance[now_n] != 1e9 and next_d + distance[now_n] < distance[next_n]:
                    distance[next_n] = next_d + distance[now_n]
                    if check == n - 1:  # n-1번 이후 반복에도 값이 갱신된다? 음순환 존재한다는 것
                        return True
    return False


distance = [1e9 for _ in range(n + 1)]
cycle = bf(1)
if cycle:
    print(-1)
else:
    for i in distance[2:]:
        print(i if i != 1e9 else -1)

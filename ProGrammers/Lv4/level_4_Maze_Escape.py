def solution(n, start, end, roads, traps):
    import heapq

    edges = [[] for _ in range(n + 1)]
    trap_idx = {t: n for n, t in enumerate(traps)}
    traps = set(traps)

    for v1, v2, w in roads:
        edges[v1].append((v2, w))
        edges[v2].append((v1, -w))  # 역방향

    heap = [(0, start, 0)]  # distance, 현위치, 현상태
    dist = {}
    answer = 0
    while heap:
        dis, here, state = heapq.heappop(heap)

        # 이미 현재 상태를 방문했었다면
        if dist.get((here, state), None):  # None은 없을때 나오는 디폴트값
            continue

        dist[(here, state)] = dis

        if here == end:
            answer = dis
            break

        direction = 1  # 방향을 나타내는 변수, 현재 위치가 트랩일 때 눌렸는지 안눌렸는지
        # 비트마스트 - 원소 포함 조회
        # state & (1 << idx) : idx만큼 밀어서 state에 포함되어있다면 true가 될것
        if here in traps and (state & (1 << trap_idx[here])):
            direction *= -1
            # 눌려있으면 here로 들어오는 간선들의 방향이 바뀌기 때문

        for there, w in edges[here]:  # 인접 노드
            # 다음 방문할 노드가 트랩이고 현재 그 트랩을 한번 방문했다면 가중치의 값 부호를 바꿈
            if there in traps and (state & (1 << trap_idx[there])):
                w *= -1

            if w * direction > 0:  # 정방향
                new_state = state
                if there in traps:
                    if state & (1 << trap_idx[there]):
                        # 트랩을 밟지 않은 상태로 바꿔준다
                        new_state = state & ~(1 << trap_idx[there])
                    else:
                        # 트랩을 밟은 상태로 바꿈
                        new_state = state | (1 << trap_idx[there])
                heapq.heappush(heap, (dis + w * direction, there, new_state))
    return answer

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])) # 5
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3])) # 4
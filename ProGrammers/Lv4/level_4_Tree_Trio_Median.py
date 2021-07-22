# 거지같은 문제네
from collections import deque
def bfs(idx, n):
    global board

    visited = [-1] * (n + 1)
    q = deque()
    q.append(idx)
    visited[idx] = 0

    _max = [0, [0], 0]  # value, node, cnt

    while q:
        old = q.popleft()
        for new in board[old]:
            # 방문한적이 없다면
            if visited[new] == -1:
                # 기존의 방문값에서 노드가 연결되어있다는것은 하나 더 길다는 뜻
                visited[new] = visited[old] + 1
                q.append(new)

                # 최댓값을 갱신해준다.
                # (최댓값, [노드], 개수)
                # 노드는 list로 만들어주는것이 길이가 같은 경우 append해주기 위해서
                if _max[0] < visited[new]:
                    _max[0] = visited[new]
                    _max[1] = [new]
                    _max[2] = 1

                # 길이가 최대랑 같은 경우는
                # node append하고
                # 개수 +1
                elif _max[0] == visited[new]:
                    _max[1].append(new)
                    _max[2] += 1

    return _max


def solution(n, edges):
    global board

    answer = 0
    max_value = -1

    board = [[] for _ in range(n + 1)]

    for i, j in edges:
        board[i].append(j)
        board[j].append(i)

    # 임의의 점 1에서 가장 먼 노드 찾기
    temp = bfs(1, n)

    # 가장 먼 노드에서 또 다른 먼 노드 찾기
    # 이때 나오는 최댓값은 지름이라고 볼 수 있다.
    temp2 = bfs(temp[1][0], n)

    # 지름의 값을 가지는 개수가 2개 이상이면 중간값은 무조건 지름이기 때문에 바로 최댓값 return
    if temp2[2] >= 2:
        return temp2[0]

    # 지름의 값을 가지는 개수가 1개일때
    else:
        # 개수가 1개일때는 임의의 점 1에서부터 진행했기 때문에 지름을 못찾을수도 있어서 한번 더 진행
        # 그때는 무조건 지름임을 보장이 가능하다
        temp3 = bfs(temp2[1][0], n)

        # 마찬가지로 개수가2개면 지름 return
        if temp3[2] >= 2:
            return temp3[0]

        # 지름이 1개면 지름에서 가까운 노드를 선택하기 때문에 -1을 해준다
        else:
            return temp3[0] - 1

print(solution(4, [[1,2],[2,3],[3,4]])) # 2
print(solution(5, [[1,5],[2,5],[3,5],[4,5]])) # 2
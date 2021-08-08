"""
방이 만들어지는 조건
1. 기존 방문한 정점을 재방문
2. 1을 만족하면서 새로운 경로로 재방문.

함정 조건
o - o
  X
o - o 의 경우 방이 2개가 만들어지지만 위 조건으로 풀었을 때
1개만 만들어진 것으로 판단된다.
그래서 이 함정 조건을 방지하기 위해 한번 움직일 때 두 칸씩 움직이도록 만듬
즉, 위 같은 경우가 발생할 수 있기 때문에 중간에 정점을 하나 더 만드는 것.
"""
def solution(arrows):
    from collections import defaultdict
    answer = 0
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    now = (0, 0)
    visited = defaultdict(int)  # 노드 방문 체크
    visited_dir = defaultdict(int)  # 노드 방문 경로 체크 ((A,B) => A->B)

    queue = [now]
    for i in arrows:
        for _ in range(2):  # 두 칸씩 이동하면서 해당 경로 모두 queue에 넣음
            nxt = (now[0] + move[i][0], now[1] + move[i][1])
            queue.append(nxt)
            now = nxt

    now = queue.pop(0)
    visited[now] = 1  # 방문 체크

    while queue:
        nxt = queue.pop(0)

        if visited[nxt]:
            if not visited_dir[(now, nxt)]:
                answer += 1
        else:
            visited[nxt] = 1

        # 경로 체크
        visited_dir[(now, nxt)] = 1
        visited_dir[(nxt, now)] = 1
        now = nxt

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])) # 3

def solution(arrows):
    point = {(0, 0)}
    line = set()
    move=[[0,2],[2,2],[2,0],[2,-2],[0,-2],[-2,-2],[-2,0],[-2,2]]
    now = (0, 0)

    for i in arrows:
        nxt = (now[0]+move[i][0], now[1]+move[i][1])
        mid = (now[0]+move[i][0]//2, now[1]+move[i][1]//2)

        point.add(nxt)
        point.add(mid)

        line.add((now, mid))
        line.add((mid, now))
        line.add((mid, nxt))
        line.add((nxt, mid))

        now = nxt
    answer = len(line)//2 - len(point)+1
    return answer if answer >= 0 else 0

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])) # 3
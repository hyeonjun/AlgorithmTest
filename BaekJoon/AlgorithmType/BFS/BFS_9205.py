def bfs():
    queue = [start]
    visited = []
    while queue:
        x, y = queue.pop(0)
        if abs(x-end[0]) + abs(y-end[1]) <= 1000: # 맥주 한 박스에 20병, 1병에 50미터 -> 1000미터까지 가능
            return True
        for nx, ny in cos:
            if [nx, ny] not in visited and abs(x-nx) + abs(y-ny) <= 1000: # 아직 들리지 않은 편의점에 갈 수 있는지
                visited.append([nx, ny])
                queue.append([nx, ny])
    return False

for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    cos = [list(map(int, input().split())) for _ in range(n)]
    end = list(map(int, input().split()))
    print("happy" if bfs() else "sad")
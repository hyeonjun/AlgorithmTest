def solution(grid):
    answer = []
    #              하    우       좌      상
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path = set()

    for d in direction:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cycle = 0
                point = (i, j)
                while True:
                    prev_point = point
                    point = (point[0] + d[0], point[1] + d[1])
                    new_path = (prev_point, point)
                    if new_path in path:  # 사이클 확인
                        break
                    else:
                        cycle += 1
                        path.add(new_path)

                    # 격자 끝으로 넘어갈 경우 반대쪽 끝으로 다시 돌아와야함
                    if point[0] >= len(grid):
                        point = (0, point[1])
                    elif point[1] >= len(grid[0]):
                        point = (point[0], 0)
                    elif point[0] < 0:
                        point = (len(grid) - 1, point[1])
                    elif point[1] < 0:
                        point = (point[0], len(grid[0]) - 1)

                    # S는 직진, L 좌, R 우
                    location = grid[point[0]][point[1]]
                    if location == "R":
                        if d == (1, 0):  # 하
                            d = (0, -1)
                        elif d == (0, 1):  # 우
                            d = (1, 0)
                        elif d == (-1, 0):
                            d = (0, 1)
                        elif d == (0, -1):
                            d = (-1, 0)
                    elif location == "L":
                        if d == (1, 0):  # 하
                            d = (0, 1)
                        elif d == (0, 1):  # 우
                            d = (-1, 0)
                        elif d == (-1, 0):
                            d = (0, -1)
                        elif d == (0, -1):
                            d = (1, 0)
                if cycle:
                    answer.append(cycle)
    return sorted(answer)

print(solution(["SL","LR"])) # [16]
print(solution(["S"])) # [1, 1, 1, 1]
print(solution(["R","R"])) # [4, 4]
"""
합벡터 V
v1 = (x1, y1) -> (x2, y2) => (x2-x1, y2-y1)
v2 = (x3, y3) -> (x4, y4) => (x4-x3, y4-y3)
V = v1 + v2 = ((x2+x4) - (x1+x3), (y2+y4) - (y1+y3))
 => 벡터들의 끝 지점에 있는 점들의 합에서 시작 지점에 있는 점들의 합을 뺀 것이
    N개의 점으로 만든 N/2개의 벡터들의 합으로 만든 벡터 V가 된다.

P에서 절반을 선택 -> 조합
입력받으면서 x와 y 좌표들의 총합을 구하고 이후 선택된 좌표들의 합을 빼자
"""
from itertools import combinations
for _ in range(int(input())):
    n = int(input())
    answer = 1e9
    coordinates = [] # 좌표
    x_total, y_total = 0, 0
    for _ in range(n):
        x, y = map(int, input().split())
        coordinates.append([x, y])
        x_total += x
        y_total += y

    comb = list(combinations(coordinates, n//2))
    for c in comb[:len(comb)//2]:
        v1_x, v1_y = 0, 0
        for x, y in c:
            v1_x += x
            v1_y += y
        # 빼줘야할 시작 지점의 합 => 총 지점들의 합 - 끝 지점 합
        v2_x = x_total - v1_x
        v2_y = y_total - v1_y

        answer = min(answer, ((v1_x - v2_x) ** 2 + (v1_y - v2_y) ** 2) ** 0.5) # z = sqrt(x^2 + y^2)

    print(answer)
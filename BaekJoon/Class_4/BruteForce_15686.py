n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

minV = 1e9
from itertools import combinations
for i in combinations(chicken, m): # 치킨집 중 m개 선택
    tmp = 0
    for j in home:
        distance = [] # 선택된 치킨집와 집 사이의 거리
        for k in i:
            distance.append(abs(j[0]-k[0]) + abs(j[1]-k[1]))
        tmp += min(distance)
    minV = min(minV, tmp)
print(minV)
n = int(input())
coordinate = []
for _ in range(n):
    a, b = map(int, input().split())
    a, b = a+500000, b+500000
    coordinate.append((a, b))

countV = [0 for _ in range(1000010)] # 각 지점 수직선의 교차 개수
countH = [0 for _ in range(1000010)] # 각 지점 수평선의 교차 개수수
for i in range(n):
    x, y = coordinate[i]
    nx, ny = coordinate[(i+1) % n]

    if x == nx: # 세로 선
        countH[min(y, ny)] += 1 # 세로 선 시작 지점, 교차 개수 + 1
        countH[max(y, ny)] -= 1 # 세로 선 끝 지점, 교차 개수 - 1
    else:
        countV[min(x, nx)] += 1 # 가로 선 시작 지점
        countV[max(x, nx)] -= 1 # 가로 선 끝 지점
# 위 교차 개수는 해당 선분에 대한 교차 개수만 구한 것
# 다각형 중간 선분들의 교차 개수 => 누적합
for i in range(1, 1000010):
    countH[i] += countH[i-1]
    countV[i] += countV[i-1]

print(max(max(countH), max(countV)))
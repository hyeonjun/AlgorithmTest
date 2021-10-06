n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    # 0번 색칠할 때, 이전 집 0번 x - 빨강
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    # 1번 색칠할 때 - 초록
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    # 2번 색칠할 때 - 파랑
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[-1]))
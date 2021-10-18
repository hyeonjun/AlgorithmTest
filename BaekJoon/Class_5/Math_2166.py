n = int(input())
coordinate = [list(map(int, input().split())) for _ in range(n)]
coordinate.append(coordinate[0])
x_to_y = 0
y_to_x = 0
for i in range(n):
    x_to_y += coordinate[i][0] * coordinate[i+1][1]
    y_to_x += coordinate[i][1] * coordinate[i+1][0]
print(round(abs(x_to_y - y_to_x)/2, 1))
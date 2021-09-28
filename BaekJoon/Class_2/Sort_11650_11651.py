# 11650
coordinate = [list(map(int, input().split())) for _ in range(int(input()))]
for a, b in sorted(coordinate, key=lambda x : (x[0], x[1])):
    print(a, b)

# 11651
coordinate = [list(map(int, input().split())) for _ in range(int(input()))]
for a, b in sorted(coordinate, key=lambda x : (x[1], x[0])):
    print(a, b)
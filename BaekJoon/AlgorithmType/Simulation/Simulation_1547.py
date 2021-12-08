m = int(input())
cup = [1, 0, 0]
for _ in range(m):
    x, y = map(int, input().split())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]
print(cup.index(1)+1)
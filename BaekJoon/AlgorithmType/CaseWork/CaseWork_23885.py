n, m = map(int, input().split())
sx, ex = map(int, input().split())
sy, ey = map(int, input().split())
if (sx, ex) == (sy, ey) or (n > 1 and m > 1 and (sx + ex) % 2 == (sy + ey) % 2):
    print('YES')
else:
    print('NO')
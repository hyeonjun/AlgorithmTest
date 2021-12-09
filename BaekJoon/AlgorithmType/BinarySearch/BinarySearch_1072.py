x, y = map(int, input().split())
z = y * 100 // x
left, right = 0, x
if z >= 99: print(-1)
else:
    while left < right:
        mid = (left + right) // 2 # 앞으로 이긴 판 수
        if (y+mid) * 100 // (x+mid) <= z:
            left = mid+1
        else:
            right = mid
    print(right)
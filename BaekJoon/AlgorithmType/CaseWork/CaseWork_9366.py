for i in range(1, int(input())+1):
    side = sorted(map(int, input().split()))
    if side[0] + side[1] <= side[2]:
        print(f'Case #{i}: invalid!')
    elif side[0] == side[1] == side[2]:
        print(f'Case #{i}: equilateral')
    elif side[0] == side[1] or side[0] == side[2] or side[1] == side[2]:
        print(f'Case #{i}: isosceles')
    else:
        print(f'Case #{i}: scalene')

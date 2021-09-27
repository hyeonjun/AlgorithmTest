while True:
    side = list(map(int, input().split()))
    side.sort()
    if max(side) == 0:
        break
    if side[0]**2 + side[1] **2 == side[2]**2:
        print("right")
    else:
        print("wrong")
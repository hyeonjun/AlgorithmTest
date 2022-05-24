coordi = []
for _ in range(3):
    coordi.append(list(map(int, input().split())))

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0: return 1
    elif tmp < 0: return -1
    else: return 0

print(ccw(*coordi[0], *coordi[1], *coordi[2]))
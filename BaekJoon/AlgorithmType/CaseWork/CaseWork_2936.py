x, y = map(int, input().split())
area = 250 * 250 / 2
a1, a2 = 0, 0
if x == 0 and y == 0:
    a1, a2 = 125, 125
elif x == 0:
    if y == 250:
        a1 = 250 / 2
    elif y > 125:
        a1, a2 = round(area / y, 2), 0
    elif y < 125:
        a1 = round(area / (250 - y), 2)
        a2 = 250 - a1
    elif y == 125:
        a1 = 250
elif y == 0:
    if x == 250:
        a2 = 250 / 2
    elif x > 125:
        a1, a2 = 0, round(area / x, 2)
    elif x < 125:
        a2 = round(area / (250 - x), 2)
        a1 = 250 - a2
    elif x == 125:
        a2 = 250
else: # 빗변
    if y < 125:
        a2 = round(250.0 - (area / x), 2)
    elif y > 125:
        a1 = round(250.0 - (area / y), 2)
print('{0:.2f} {1:.2f}'.format(a1, a2))
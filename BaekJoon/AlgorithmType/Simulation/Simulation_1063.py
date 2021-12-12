direction = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}
king, rock, n = input().split()
king, rock = list(king), list(rock)
king_x, king_y = ord(king[0])-ord('A'), int(king[1]) - 1
rock_x, rock_y = ord(rock[0])-ord('A'), int(rock[1]) - 1
for _ in range(int(n)):
    d = direction[input()]
    nx, ny = king_x+d[0], king_y+d[1]
    if nx < 0 or nx > 7 or ny < 0 or ny > 7:
        continue
    if nx == rock_x and ny == rock_y:
        r_x, r_y = rock_x + d[0], rock_y + d[1]
        if r_x < 0 or r_x > 7 or r_y < 0 or r_y > 7:
            continue
        rock_x, rock_y = r_x, r_y
    king_x, king_y = nx, ny

print("{0}{1}".format(chr(king_x + ord('A')), king_y+1))
print("{0}{1}".format(chr(rock_x + ord('A')), rock_y+1))
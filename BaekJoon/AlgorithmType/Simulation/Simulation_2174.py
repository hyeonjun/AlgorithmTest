import sys
input = sys.stdin.readline
a, b = map(int, input().split())
n, m = map(int, input().split())
robots = []
board = [[0 for _ in range(a)] for _ in range(b)]

direction = {'N':0, 'E':1, 'S':2, 'W':3}
direct = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(n):
    x, y, d = input().split()
    r, c = b - int(y), int(x) - 1
    robots.append([r, c, direction[d]])
    board[r][c] = i+1

flag = False
for i in range(m):
    robot, cmd, loop = input().split()
    robot, loop = int(robot), int(loop)
    r, c, d = robots[robot-1]
    if cmd == 'L' or cmd == 'R':
        d = (d + loop) % 4
        if loop % 2 and cmd == 'L':
            d = (d + 2) % 4
        robots[robot-1] = [r, c, d]
    else:
        dr, dc = direct[d]
        for _ in range(loop):
            if 0 <= r+dr < b and 0 <= c+dc < a:
                if board[r+dr][c+dc]:
                    flag = True
                    print('Robot {0} crashes into robot {1}'.format(board[r][c], board[r+dr][c+dc]))
                    break
                else:
                    board[r][c], board[r+dr][c+dc] = 0, robot
                    r, c = r+dr, c+dc
                    robots[robot-1] = [r, c, d]
            else:
                flag = True
                print('Robot {0} crashes into the wall'.format(board[r][c]))
                break
    if flag:
        break
if not flag:
    print('OK')
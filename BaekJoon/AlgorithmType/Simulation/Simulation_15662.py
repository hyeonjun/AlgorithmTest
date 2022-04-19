from collections import deque

n = int(input())
gears = {}
for i in range(1, n+1):
    gears[i] = deque(list(map(int, input())))

def checkRight(start, d):
    # 끝이거나 맞닿은 극이 같으면 회전 X
    if start > n or gears[start-1][2] == gears[start][6]:
        return

    checkRight(start+1, -d)
    gears[start].rotate(d)


def checkLeft(start, d):
    # 첫번째 톱니바퀴이거나 극이 같으면 회전 X
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return

    checkLeft(start-1, -d)
    gears[start].rotate(d)


for _ in range(int(input())):
    num, dirs = map(int, input().split())
    # num번 톱니바퀴가 회전한 방향의 반대방향으로 회전
    checkRight(num+1, -dirs)
    checkLeft(num-1, -dirs)
    gears[num].rotate(dirs)

print(sum(val[0] for val in gears.values()))
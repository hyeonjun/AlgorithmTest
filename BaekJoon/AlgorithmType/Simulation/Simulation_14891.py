"""
1. 톱니바퀴를 움직이기 전에 인접 톱니바퀴 중 움직일 수 있는 톱니바퀴가 있는지 검사
2. 인접 톱니바퀴가 움직일 수 있으면 해당 톱니바퀴의 인접 톱니바퀴도 움직일 수 있는지 검사
3. 회전 여부를 결정짓는 인접 톱니바퀴의 톱날은 index 2, 6
4. 주어진 톱니바퀴는 일단 회전한다.
5. 인접 톱니바퀴는 주어진 톱니바퀴는 반대방향으로 회전
6. 시계방향은 1, 반시계방향은 -1
"""
from collections import deque

def checkRight(start, dirs):
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return

    if gears[start-1][2] != gears[start][6]:
        checkRight(start+1, -dirs)
        gears[start].rotate(dirs)

def checkLeft(start, dirs):
    if start < 1 or gears[start][2] == gears[start+1][6]:
        return

    if gears[start][2] != gears[start+1][6]:
        checkLeft(start-1, -dirs)
        gears[start].rotate(dirs)

gears = {}
for i in range(1, 5):
    gears[i] = deque(list(map(int, input()))) # 12시방향부터 시계방향 순서대로 주어진다.

for _ in range(int(input())):
    num,  dirs = map(int, input().split())
    checkRight(num+1, -dirs)
    checkLeft(num-1, -dirs)
    gears[num].rotate(dirs)

print(sum([(2**i) * gears[i+1][0] for i in range(4)]))
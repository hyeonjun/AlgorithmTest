import sys
input = sys.stdin.readline
r, c, t = map(int, input().split())
matrix = []
ac = [] # 공기 청정기
for i in range(r):
    tmp = list(map(int, input().split()))
    matrix.append(tmp)
    for j in range(c):
       if tmp[j] == -1: # 공기청정기
           ac.append((i, j))

up1, up2 = ac[0] # 공기청정기 위쪽
down1, down2 = ac[1] # 공기청정기 아래쪽
#             아래      위     오       왼
direction = [(1,0), (-1,0), (0,1), (0,-1)]


def dust():  # 미세먼지 확산
    tmp = [[0 for _ in range(c)] for _ in range(r)] # 미세먼지 인접한 곳에 또 다른 미세먼지가 있어 확산이 겹칠 수 있기 때문에
    tmp[up1][up2], tmp[down1][down2] = -1, -1
    for x in range(r):
        for y in range(c):
            if matrix[x][y] > 0: # 미세먼지 위치
                cnt = 0 # 인접 개수
                for dx, dy in direction: # 확산 위치
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < r and 0 <= ny < c and tmp[nx][ny] != -1:
                        tmp[nx][ny] += matrix[x][y] // 5 # 확산
                        cnt += 1 # 확산된 개수
                tmp[x][y] += matrix[x][y] - matrix[x][y] // 5 * cnt # 확산되고 남은거
    return tmp

def cleaner(x, y, dir):  # 공기 청정
    tmp = [m[:] for m in matrix]
    matrix[x][y] = 0
    clean_x, clean_y = x, y-1
    for i in dir:
        while True:
            nx, ny = x+direction[i][0], y+direction[i][1]
            if nx == clean_x and ny == clean_y: # 공기청정기를 만나면 끝
                return
            if 0 <= nx < r and 0 <= ny < c:
                matrix[nx][ny] = tmp[x][y] # 미세먼지 움직임
            else: # 끝까지 갔으면 다음 방향
                break
            x, y = nx, ny # 공기청정기 바람 움직임

for _ in range(t):
    matrix = dust()
    cleaner(up1, up2+1, [2, 1, 3, 0]) # 위쪽 : 오른쪽 -> 위쪽 -> 왼쪽 -> 아래쪽
    cleaner(down1, down2+1, [2, 0, 3, 1]) # 아래쪽 : 오른쪽 -> 아래쪽 -> 왼쪽 -> 위쪽

result = 2
for i in matrix:
    result += sum(i)
print(result)
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 # 사과
times = {}
for _ in range(int(input())):
    x, c = input().split()
    times[int(x)] = c

#             상       우       하      좌
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def change(d, c): # 방향
    return (d-1) % 4 if c == "L" else (d+1) % 4

def start():
    d = 1 # 초기 방향
    answer = 1
    x, y = 0, 0
    visited = [(0, 0)] # 뱀
    board[0][0] = 2
    while True:
        x, y = x+direction[d][0], y+direction[d][1]
        if 0 <= x < n and 0 <= y < n and board[x][y] != 2:
            if not board[x][y] == 1: # 사과
                tx, ty = visited.pop(0)
                board[tx][ty] = 0
            board[x][y] = 2
            visited.append((x, y))
            if answer in times.keys():
                d = change(d, times[answer])
            answer += 1
        else:
            return answer
print(start())
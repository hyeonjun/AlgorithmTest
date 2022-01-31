"""
검 흰 검
흰 검 흰
검 흰 검
"""
import sys
input=sys.stdin.readline
n = int(input())
board = []
candiW, candiB = [], []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            if (i+j) % 2 == 0: # 흰칸
                candiW.append((i, j))
            else: # 검은칸
                candiB.append((i, j))
    board.append(tmp)

direction = [(1,1), (-1,1), (-1,-1), (1,-1)]
def check(i, j, flag):
    for dx, dy in direction:
        x, y = i, j
        while True:
            if 0 <= x < n and 0 <= y < n:
                visited[x][y] += flag
            else:
                break
            x, y = x+dx, y+dy

def dfs(idx, cnt, candi):
    global result
    if idx >= len(candi):
        result = max(result, cnt)
        return
    x, y = candi[idx]
    if not visited[x][y]:
        check(x, y, 1)
        dfs(idx+1, cnt+1, candi)
        check(x, y, -1)
        dfs(idx+1, cnt, candi)
    else:
        dfs(idx+1, cnt, candi)


answer = 0

result = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
dfs(0, 0, candiW)
answer += result

result = 0
visited = [[0 for _ in range(n)] for _ in range(n)]
dfs(0, 0, candiB)
answer += result

print(answer)
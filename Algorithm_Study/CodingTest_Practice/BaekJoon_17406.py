# 배열 돌리기 4
from copy import deepcopy
board = [
[1, 2, 3, 2, 5, 6],
[3, 8, 7, 2, 1, 3],
[8, 2, 3, 1, 4, 5],
[3, 4, 5, 1, 1, 1],
[9, 3, 2, 1, 4, 3]]
k = 2
Q = [(3,4,2),(4,2,1)]

def value(arr):
    return min([sum(i) for i in arr])

def convert(arr, qry):
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    r, c, s = qry
    r, c, = r - 1, c - 1
    new_arr = deepcopy(arr)
    for i in range(1, s + 1):
        rr, cc = r - i, c + i
        for w in range(4):  # 4방향
            for d in range(i * 2):
                nx, ny = rr + dx[w], cc + dy[w]
                new_arr[nx][ny] = arr[rr][cc]
                rr, cc = nx, ny
    return new_arr

ans = 1e7
def dfs(arr, qry, k):
    global ans
    if sum(qry) == k:
        ans = min(ans, value(arr))
        return
    for i in range(k):
        if qry[i]:
            continue
        new_arr = convert(arr, Q[i])
        qry[i] = 1 # 회전 했는지 확인
        dfs(new_arr, qry, k)
        qry[i] = 0
    return ans


dfs(board, [0 for i in range(k)], k)
print(ans)
# 왼 위 [1,2] 오 아래 [5,6]
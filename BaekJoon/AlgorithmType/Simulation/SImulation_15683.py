from copy import deepcopy
n, m = map(int, input().split())
board, cctv = [], []
count, answer = 0, 1e9
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] not in [0, 6]:
            cctv.append((i, j, tmp[j]))
            count += 1
    board.append(tmp)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#                      1번                 2번                        3번
direct = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]],
          [[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
#                               4번                            5번

def check(x, y, arr, d):
    for i in d:
        nx, ny = x, y
        while True:
            nx += direction[i][0]
            ny += direction[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 6:
                    break
                elif arr[nx][ny] == 0:
                    arr[nx][ny] = '#'
            else:
                break

def dfs(arr, idx):
    global answer
    temp = deepcopy(arr)
    if idx == count:
        result = 0
        for i in range(n):
            result += temp[i].count(0)
        answer = min(result, answer)
        return

    x, y, d = cctv[idx]
    for i in direct[d]:
        check(x, y, temp, i)
        dfs(temp, idx+1)
        temp = deepcopy(arr)


dfs(board, 0)
print(answer)
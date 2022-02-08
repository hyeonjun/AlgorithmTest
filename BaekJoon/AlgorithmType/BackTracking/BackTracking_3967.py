board = []
visited = [False for _ in range(13)] # 알파벳 체크
arr = []
for i in range(5):
    tmp = list(input())
    for j in range(len(tmp)):
        if tmp[j] == 'x':
            arr.append((i, j))
        elif tmp[j] != '.':
            visited[ord(tmp[j]) - ord('A') + 1] = True
    board.append(tmp)
count = len(arr)

points = [
    [[0, 4], [1, 3], [2, 2], [3, 1]],
    [[3, 1], [3, 3], [3, 5], [3, 7]],
    [[0, 4], [1, 5], [2, 6], [3, 7]],
    [[1, 1], [1, 3], [1, 5], [1, 7]],
    [[1, 1], [2, 2], [3, 3], [4, 4]],
    [[4, 4], [3, 5], [2, 6], [1, 7]]
]

def check():
    for point in points:
        s = 0
        for x, y in point:
            s += ord(board[x][y]) - ord('A') + 1
        if s != 26:
            return False
    return True

def dfs(depth, idx):
    global board
    if depth == count:
        if check():
            for b in board:
                print(''.join(b))
            exit()
        return

    for i in range(1, 13):
        if visited[i]: continue
        x, y = arr[idx]
        visited[i] = True
        board[x][y] = chr(i+64)
        dfs(depth+1, idx+1)
        board[x][y] = 'x'
        visited[i] = False

dfs(0, 0)
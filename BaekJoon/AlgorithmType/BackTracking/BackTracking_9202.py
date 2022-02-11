# BackTracking, 29648ms
# DataStructure Trie & BackTracking Reference - DataStructures/DataStructures_Trie_9202.py
import sys
input=sys.stdin.readline
direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
score = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}

w = int(input())
words = [input().strip() for _ in range(w)]
_ = input() # 빈 줄

def dfs(x, y, word, idx, wi):
    global maxScore, maxString, cnt
    if visited[wi]: return # 이미 찾았으면

    if idx == len(word)-1:
        if board[x][y] == word[idx]: # 마지막 단어도 같으면
            maxScore += score[len(word)]
            cnt += 1
            if len(word) > len(maxString):
                maxString = word
            elif len(word) == len(maxString):
                maxString = sorted([word, maxString])[0]
            visited[wi] = True
        return

    if board[x][y] != word[idx]: # idx번째 알파벳이 다르면
        return

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or check[nx][ny]:
            continue
        check[nx][ny] = 1
        dfs(nx, ny, word, idx+1, wi)
        check[nx][ny] = 0

b = int(input())
for t in range(b):
    board = [input().strip() for _ in range(4)]
    maxScore = 0
    maxString = ''
    cnt = 0
    visited = [False for _ in range(w)]

    for i in range(w):
        check = [[0 for _ in range(4)] for _ in range(4)]
        for n in range(16):
            r, c = n // 4, n % 4
            check[r][c] = 1
            dfs(r, c, words[i], 0, i)
            check[r][c] = 0
    print(maxScore, maxString, cnt)

    if t == b-1:
        break
    _ = input()

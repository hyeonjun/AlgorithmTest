# Trie & BackTracking, 9224ms
# BackTracking Reference - BackTracking/BackTracking_9202.py
from collections import deque
import sys
input=sys.stdin.readline

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}
        self.check = False

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node(w)
            cur = cur.child[w]
        cur.data = word

    def search(self, word):
        cur = self.head
        for w in word:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        if cur.check or cur.data == None: # 이미 찾았거나 문자가 없으면
            return False
        cur.check = True
        return True

    def initialize(self):
        queue = deque(self.head.child.values())
        while queue:
            cur = queue.popleft()
            if cur.data != None:
                cur.check = False
            queue.extend(cur.child.values())

direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, -1], [-1, 1], [1, 1]]
score = {1:0, 2:0, 3:1, 4:1, 5:2, 6:3, 7:5, 8:11}

w = int(input())
trie = Trie()
for _ in range(w):
    trie.insert(input().strip())
input()

def dfs(x, y, string, length, node):
    global maxScore, maxString, cnt
    if trie.search(string): # 단어 찾았으면
        maxScore += score[length]
        cnt += 1
        if length > len(maxString):
            maxString = string
        elif length == len(maxString) and string < maxString:
            maxString = string

    if length == 8: # 최대 글자 수 8
        return

    for dx, dy in direction:
        nx, ny = x+dx, y+dy
        if 0 > nx or nx >= 4 or 0 > ny or ny >= 4 or visited[nx][ny]:
            continue
        if board[nx][ny] not in node.child:
            continue
        # 다음 문자가 존재하면
        visited[nx][ny] = True
        # 그 다음 문자 찾기
        dfs(nx, ny, string+board[nx][ny], length+1, node.child[board[nx][ny]])
        visited[nx][ny] = False

b = int(input())
for t in range(b):
    board = [input().strip() for _ in range(4)]
    maxScore = 0
    maxString = ''
    cnt = 0
    visited = [[False for _ in range(4)] for _ in range(4)]
    trie.initialize()
    for n in range(16):
        r, c = n // 4, n % 4
        if board[r][c] in trie.head.child: # 첫 문자 찾았으면
            visited[r][c] = True
            dfs(r, c, board[r][c], 1, trie.head.child[board[r][c]]) # 다음 문자 찾기
            visited[r][c] = False
    print(maxScore, maxString, cnt)
    if t == b-1:
        break
    input()

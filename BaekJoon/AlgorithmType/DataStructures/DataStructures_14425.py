# defaultdict, 376ms
from collections import defaultdict
n, m = map(int, input().split())
stringDict = defaultdict(int)
for _ in range(n):
    string = input()
    stringDict[string] = 1
answer = 0
for _ in range(m):
    string = input()
    answer += stringDict[string]
print(answer)

# trie, 5852ms
class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                cur.child[ch] = Node(ch)
            cur = cur.child[ch]
        cur.child['*'] = True

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur.child:
                return False
            cur = cur.child[ch]
        if '*' in cur.child:
            return True

n, m = map(int, input().split())
trie = Trie()
answer = 0
for _ in range(n):
    string = input()
    trie.insert(string)

for _ in range(m):
    string = input()
    if trie.search(string):
        answer += 1
print(answer)
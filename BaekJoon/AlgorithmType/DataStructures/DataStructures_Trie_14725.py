class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, word):
        cur = self.head
        for w in word:
            if w not in cur:
                cur[w] = {} # 자식 노드
            cur = cur[w]
        cur[0] = True # 리프 노드 표시

    def travel(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)
        for c in cur_child:
            print('--'*level + c)
            self.travel(level+1, cur[c])

trie = Trie()
for _ in range(int(input())):
    d = list(input().split())
    trie.insert(d[1:])
trie.travel(0, trie.head)
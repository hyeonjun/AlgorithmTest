# Sort, 460ms
for _ in range(int(input())):
    n = int(input())
    numbers = sorted(input() for _ in range(n))
    flag = True
    for i in range(n-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            flag = False
            break
    print('YES' if flag else 'NO')

# Trie, 1332ms
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}

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
            cur = cur.child[w]
        if cur.child:
            return False
        else:
            return True

for _ in range(int(input())):
    trie = Trie()
    numbers = []
    for _ in range(int(input())):
        num = input()
        numbers.append(num)
        trie.insert(num)

    flag = True
    for num in sorted(numbers):
        if not trie.search(num):
            flag = False
            break
    print('YES' if flag else 'NO')
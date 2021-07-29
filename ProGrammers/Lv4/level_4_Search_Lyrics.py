import sys
sys.setrecursionlimit(100001)
def make_trie(trie, words):
    for word in words:
        cur = trie
        l = len(word)
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['?'].append(l)
            else:
                cur[w] = {}
                cur = cur[w]
                cur['?'] = [l]
    return trie

def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['?'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)
    return count

def solution(words, queries): # 아래보다 조금 더 빠름
    answer = []

    rev_words, counted = [], []
    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w))

    trie = make_trie({}, words)
    rev_trie = make_trie({}, rev_words)

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        elif query[0] == '?':
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?':
            answer.append(search_trie(trie, query, len(query)))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries)) # [3, 2, 4, 1, 0]

from collections import defaultdict
class Node:
    def __init__(self, data):
        self.data = data # 현재 노드의 값
        self.count = 0 # 현재 노드가 소유한 모든 자식 노드 수
        self.child = {} # Trie 자료구조

class Trie:
    def __init__(self):
        self.head = Node(None) # 최상위 노드 생성

    def insert(self, string):
        cur = self.head # 최상위 노드 불러옴
        cur.count += 1

        for c in string: # 입력받은 단어 한글자씩 확인
            if c not in cur.child: # 현재 노드의 자식 노드 중 c가 없다면
                cur.child[c] = Node(c) # 현재 노드의 자식[c]에 자식노드[c] 생성
            cur = cur.child[c] # 현 노드를 자식노드로 변경
            cur.count += 1

    def count(self, prefix):
        cur = self.head # 최상위 노드
        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c] # 있으면 자식 노드로 이동하여
        return cur.count # 자식노드에 도착하여 해당 노드의 count 반환

def create_trie(words, reverse=False):
    trie_dic = defaultdict(Trie)
    for word in words:
        if reverse:
            word = word[::-1]
        trie_dic[len(word)].insert(word)
    return trie_dic

def search(tries, rev_tries, query):
    new_query = query.replace('?', '')
    if query[0] == '?': # 첫 문자가 ?
        return rev_tries[len(query)].count(new_query[::-1])
    else:
        return tries[len(query)].count(new_query)

def solution(words, queries):
    answer = []
    tries = create_trie(words) # Trie 생성
    rev_tries = create_trie(words, True)

    for q in queries:
        answer.append(search(tries, rev_tries, q))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries)) # [3, 2, 4, 1, 0]





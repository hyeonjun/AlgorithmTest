class Trie():
    def __init__(self):
        self.next = dict()
        self.value = 0

def solution(words):
    answer = 0
    tree = Trie()
    for w in words:
        sub = tree
        for i, v in enumerate(w):
            sub.value += 1
            if v not in sub.next:
                sub.next[v] = Trie()
            sub = sub.next[v]
            if i == len(w) - 1:
                sub.value += 1

    for w in words:
        sub = tree
        cnt = 0
        for i, v in enumerate(w):
            if sub.value == 1:
                answer += cnt
                break
            elif i == len(w) - 1:
                answer += cnt + 1
                break
            else:
                sub = sub.next[v]
                cnt += 1
    return answer

print(solution(["go", "gone", "guild"])) # 7
print(solution(["abc", "def", "ghi", "jklm"])) # 4
print(solution(["word", "war", "warrior", "world"])) # 15

def solution(words):
    Trie = {}  ## dictionary 형태로 Trie를 만듭니다.
    for word in words:
        cur_Trie = Trie
        for w in word:
            cur_Trie.setdefault(w, [0, {}])
            cur_Trie[w][0] += 1  ## Trie를 만들어 가면서 하위 트리가 몇개인지 추가합니다.
            cur_Trie = cur_Trie[w][1]

    result = 0
    for word in words:
        cur_Trie = Trie
        for i in range(len(word)):
            if cur_Trie[word[i]][0] == 1:  ## Trie를 탐색하다가 하위트리가 한개이면 결과에 추가합니다.
                break
            cur_Trie = cur_Trie[word[i]][1]
        result += i + 1
    return result

print(solution(["go", "gone", "guild"])) # 7
print(solution(["abc", "def", "ghi", "jklm"])) # 4
print(solution(["word", "war", "warrior", "world"])) # 15
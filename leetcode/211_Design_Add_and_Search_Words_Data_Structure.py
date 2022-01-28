"""
Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

Output
    [null,null,null,null,false,true,true,true]

Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True
"""
# Trie
from collections import defaultdict

class Node:
    def __init__(self):
        self.EndWord = False
        self.child = defaultdict(Node)


class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        cur = self.head
        for ch in word:
            cur = cur.child[ch]
        cur.EndWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.EndWord

            if word[i] == '.':
                for ch in node.child:
                    if dfs(node.child[ch], i + 1):
                        return True

            if word[i] in node.child:
                return dfs(node.child[word[i]], i + 1)

            return False

        return dfs(self.head, 0)
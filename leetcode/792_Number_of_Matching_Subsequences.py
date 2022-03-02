# Trie
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        from collections import defaultdict
        trie = defaultdict(list)
        answer= 0

        for w in words:
            trie[w[0]].append(w)

        for s in S:
            word_list = trie[s]
            trie[s] = []
            for word in word_list:
                if len(word) == 1:
                    answer += 1
                else:
                    trie[word[1]].append(word[1:])
        return answer

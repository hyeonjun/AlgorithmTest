class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque, defaultdict
        wordList = set(wordList)

        candidate = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                candidate[word[:i]+'_'+word[i+1:]].append(word)

        visited = set()
        visited.add(beginWord)
        queue = deque([[beginWord, 1]])
        while queue:
            x, cnt = queue.popleft()
            if x == endWord:
                return cnt
            for i in range(len(beginWord)):
                for candi in candidate[x[:i] + '_' + x[i+1:]]:
                    if candi not in visited:
                        queue.append([candi, cnt+1])
                        visited.add(candi)
        return 0

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict, deque
        b = len(beginWord)
        candidate = defaultdict(list)
        for word in wordList:
            for i in range(b):
                candidate[word[:i]+'_'+word[i+1:]].append(word)

        queue = deque([(beginWord, [beginWord])])
        visited = set([beginWord])
        answer = []

        while queue:
            flag = False
            check = set()
            for _ in range(len(queue)):
                x, path = queue.popleft()
                for i in range(b):
                    for candi in candidate[x[:i]+'_'+x[i+1:]]:
                        if candi in visited:
                            continue
                        if candi == endWord:
                            path.append(endWord)
                            answer.append(path[:])
                            path.pop()
                            flag = True
                            continue

                        check.add(candi)
                        path.append(candi)
                        queue.append((candi, path[:]))
                        path.pop()
            if flag:
                return answer
            visited.update(check)
        return answer

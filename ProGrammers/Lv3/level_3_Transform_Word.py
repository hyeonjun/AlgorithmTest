def solution(begin, target, words): # BFS
    if target not in words:
        return 0

    def diff(cur_word, words):
        candidates = []
        for w in words:
            d = 0
            for x, y in zip(cur_word, w):
                if x != y:
                    d += 1
            if d == 1:
                candidates.append(w)
        return candidates

    visited = [begin]
    queue = [[begin, 0]]
    while queue:
        cur_word, count = queue.pop(0)
        if cur_word == target:
            return count
        for word in diff(cur_word, words):
            if word not in visited:
                queue.append([word, count + 1])
                visited.append(word)
    return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"])) # 0

def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [0 for _ in words]
    stack = [begin]
    answer = 0

    while stack:
        cur_word = stack.pop()
        if cur_word == target:
            return answer

        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i]!=cur_word[i]]) == 1:
                if visited[w] == 0:
                    visited[w] = 1
                    stack.append(words[w])
        answer += 1
    return 0
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"])) # 0
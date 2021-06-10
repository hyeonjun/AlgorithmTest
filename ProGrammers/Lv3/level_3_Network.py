def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    def bfs(i, computers, visited):
        queue = [i]
        while queue:
            x = queue.pop(0)
            for c in range(len(computers[x])):
                if computers[x][c] == 1 and visited[c] == False:
                    visited[c] = True
                    queue.append(c)
        return
    for i in range(n):
        if visited[i] == False:
            bfs(i, computers, visited)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, 	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1

def solution(n, computers):
    answer = 0
    visited = [False] * n

    def dfs(i, computers, visited):
        stack = [i]
        while stack:
            x = stack.pop()
            for c in range(len(computers[x])):
                if computers[x][c] == 1 and visited[c] == False:
                    visited[c] = True
                    stack.append(c)
        return
    for i in range(n):
        if visited[i] == False:
            dfs(i, computers, visited)
            answer += 1
    return answer
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, 	[[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1

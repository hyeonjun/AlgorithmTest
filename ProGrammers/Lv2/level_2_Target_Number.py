def solution(numbers, target):
    node = [0]
    for i in numbers:
        sub = []
        for j in node:
            sub.extend([j+i, j-i])
        node = sub
    return node.count(target)

print(solution([1,1,1,1,1], 3)) # 5

def solution(numbers, target): # BFS
    answer = 0
    need_visit = [[numbers[0], 0], [-1*numbers[0], 0]]
    while need_visit:
        node, idx = need_visit.pop(0)
        idx += 1
        if idx < len(numbers):
            need_visit.extend([[node+numbers[idx], idx], [node-numbers[idx], idx]])
        else:
            if node == target:
                answer+=1
    return answer

print(solution([1,1,1,1,1], 3)) # 5

def solution(numbers, target): # DFS
    answer = 0
    need_visit = [[numbers[0], 0], [-1*numbers[0], 0]]
    while need_visit:
        node, idx = need_visit.pop()
        idx += 1
        if idx < len(numbers):
            need_visit.extend([[node+numbers[idx], idx], [node-numbers[idx], idx]])
        else:
            if node == target:
                answer+=1
    return answer

print(solution([1,1,1,1,1], 3)) # 5



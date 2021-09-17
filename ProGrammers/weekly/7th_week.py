def solution(enter, leave):
    answer = [set() for _ in range(len(enter)+1)]
    room = []
    e, l = 0, 0
    while e < len(enter) or l < len(leave):
        if leave[l] not in room:
            for r in room:
                answer[enter[e]].add(r)
            room.append(enter[e])
            e += 1
        else:
            room.remove(leave[l])
            l += 1
    for i, v in enumerate(answer):
        for j in v:
            answer[j].add(i)
    return list(len(i) for i in answer[1:])

print(solution([1,4,2,3], [2,1,3,4])) # [2,2,1,3]
print(solution([3,2,1],	[2,1,3])) # [1,1,2]
print(solution([3,2,1],	[1,3,2])) # [2,2,2]
print(solution([1,4,2,3], [2,1,4,3])) # [2,2,0,2]

def solution(enter, leave):
    answer = [[] for _ in range(len(enter)+1)]
    room = []
    e, l = 0, 0
    while e < len(enter) or l < len(leave):
        if leave[l] not in room:
            room.append(enter[e])
            e += 1
        else:
            for r1 in room:
                answer[r1].extend(room)
            room.remove(leave[l])
            l += 1

    return list(len(set(i))-1 for i in answer[1:])

print(solution([1,4,2,3], [2,1,3,4])) # [2,2,1,3]
print(solution([3,2,1],	[2,1,3])) # [1,1,2]
print(solution([3,2,1],	[1,3,2])) # [2,2,2]
print(solution([1,4,2,3], [2,1,4,3])) # [2,2,0,2]

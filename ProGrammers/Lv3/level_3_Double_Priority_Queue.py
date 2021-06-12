def solution(operations):
    answer = []
    for i in operations:
        cmd, data = i.split(" ")
        if cmd == "I":
            answer.append(int(data))
        else:
            if len(answer) > 0:
                if data == "1":
                    answer.pop()
                else:
                    answer.pop(0)
        answer.sort()
        print(answer)
    return [max(answer), min(answer)] if len(answer) != 0 else [0,0]

# print(solution(["I 16","D 1"])) # [0,0]
# print(solution(["I 7","I 5","I -5","D -1"])) # [7,5]
# [333, -45]
# print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

def solution(operations):
    import heapq
    answer = []
    for i in operations:
        cmd, data = i.split(" ")
        if cmd == 'I':
            heapq.heappush(answer, int(data))
        else:
            if len(answer) > 0:
                if data == '1':
                    # heapq.nlargest(n, iterable)
                    # n=개수
                    # iterable=배열
                    # list형으로 출력됨
                    answer.pop(answer.index(heapq.nlargest(1,answer)[0]))
                else:
                    heapq.heappop(answer)
    # return [max(answer), min(answer)] if answer != 0 else [0,0]
    return [heapq.nlargest(1, answer)[0], heapq.nsmallest(1, answer)[0]] if len(answer) != 0 else [0,0]
print(solution(["I 16","D 1"])) # [0,0]
print(solution(["I 7","I 5","I -5","D -1"])) # [7,5]
# [333, -45]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

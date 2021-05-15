def solution(priorities, location):
    answer = 0
    # 맨 앞에 있는 것을 꺼냄
    # 꺼낸 것보다 하나라도 높은 우선순위가 있으면 맨뒤로 다시 넣음
    # 그렇지 않으면 인쇄
    while True:
        current = priorities[0]
        if len(priorities) <= 1:
            return answer+1
        else:
            maxV = max(priorities[1:])
            if maxV > current:
                priorities.remove(current)
                priorities.append(current)
                location = len(priorities)-1 if location == 0 else location - 1
            else:
                priorities.remove(current)
                answer += 1
                if location == 0:
                    return answer
                else:
                    location -= 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))

def solution(priorities, location):
    printer = [(i, v) for i, v in enumerate(priorities)]
    answer = 0

    while True:
        current = printer.pop(0) # 맨 앞에꺼 빼기
        # maxV = max(printer, key= lambda x: x[1])
        # if current[1] < maxV[1]:
        #     printer.append(current)
        if any(current[1] < p[1] for p in printer):
            printer.append(current)
        else:
            answer += 1
            if current[0] == location:
                return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
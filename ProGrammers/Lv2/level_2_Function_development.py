def solution(progresses, speeds):
    time = [0] * (len(progresses))
    for i in range(len(progresses)):
        T = (100 - progresses[i]) // speeds[i]
        C = T * speeds[i] + progresses[i]
        T = T if C >= 100 else T+1
        time[i] = time[i-1] if time[i-1] > T else T
    check = {}
    for i in time:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1
    return list(check.values())

# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))

def solution(progresses, speeds):
    answer = []
    for p, s in zip(progresses, speeds):
        if len(answer) == 0 or answer[-1][0]< (100-p)//s:
            answer.append([(100-p)//s, 1])
        else:
            answer[-1][1] += 1
    return [q[1] for q in answer]

print(solution([93, 30, 55], [1, 30, 5]))
print()
print(solution([95, 90, 99, 99, 80, 99], [1,1,1,1,1,1]))

def solution(N, stages):
    checker = {i:0 for i in range(N+1)}
    for i in range(len(stages)):
        if stages[i] in checker:
            checker[stages[i]] += 1
    print(checker)
    failure = []
    reach_user = 0
    for i in range(N):
        try:
            fail_count = checker[i + 1]
            reach_user += checker[i]
            failure.append([i + 1, fail_count / (len(stages) - reach_user)])
        except:
            failure.append([i + 1, 0])
    failure.sort(key=lambda x: x[1], reverse=True)

    return [failure[i][0] for i in range(len(failure))]

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, [4,4,4,4,4]))
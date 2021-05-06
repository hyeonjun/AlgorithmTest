def solution(N, stages):
    checker = {}
    for i in range(N + 1):
        checker[i] = 0
    for i in range(len(stages)):
        if stages[i] in checker:
            checker[stages[i]] += 1

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

